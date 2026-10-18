# sub_00B2FFDC

- RVA: `0x00B2FFDC`–`0x00B30002` (길이 `38` bytes)
- VA: `0x0000000140B2FFDC`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A3CFC`
- 디코드: `11`개 명령, `38/38` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x00B2FFFD` → [WmipStaticInstanceNameSize + 0x47](../9E/WmipStaticInstanceNameSize_function_009E1330.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00B2FFDC  4D 8B 19                        mov r11, qword ptr [r9]
00B2FFDF  4C 8B C0                        mov r8, rax
00B2FFE2  49 FF C0                        inc r8
00B2FFE5  66 43 39 1C 43                  cmp word ptr [r11 + r8*2], bx
00B2FFEA  75 F6                           jne 0x140b2ffe2
00B2FFEC  42 8D 14 42                     lea edx, [rdx + r8*2]
00B2FFF0  49 83 C1 08                     add r9, 8
00B2FFF4  83 C2 04                        add edx, 4
00B2FFF7  49 83 EA 01                     sub r10, 1
00B2FFFB  75 DF                           jne 0x140b2ffdc
00B2FFFD  E9 75 13 EB FF                  jmp 0x1409e1377
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall sub_00B2FFDC(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 v_r10;

loc_00B2FFE2:
    a3 = (result) + 1;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(a4) + a3 * 2)) != ((unsigned __int16)(v_rbx))) goto loc_00B2FFE2;
    a4 = (a4) + (8);
    a2 = (unsigned int)((a2 + a3 * 2) + (4));
    v_r10 = (v_r10) - (1);
    if (condition_is_not_equal) goto loc_00B2FFDC;
}
```

## 5. (Beta) C Style

```c
void sub_00B2FFDC(int64_t Arg1, void *Arg2, int64_t Arg3, void *Arg4)
{
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t local_r10;

loc_00B2FFE2:
    Arg3 = (result) + 1;
    if ((*(uint16_t *)(*(uint64_t *)(arg4) + Arg3 * 2)) != ((uint16_t)(local_rbx))) goto loc_00B2FFE2;
    Arg4 = (Arg4) + (8);
    Arg2 = (uint32_t)((Arg2 + Arg3 * 2) + (4));
    local_r10 = (local_r10) - (1);
    if (condition_is_not_equal) goto loc_00B2FFDC;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x0 + r8*2` | `32` | `R` |
| `Arg4` | `+ 0x0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00B2FFDC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B2FFDC[BB_00B2FFDC]
  bb_00B2FFE2[BB_00B2FFE2]
  bb_00B2FFEC[BB_00B2FFEC]
  bb_00B2FFFD[BB_00B2FFFD]
  bb_00B2FFDC -->|flow| bb_00B2FFE2
  bb_00B2FFE2 -->|branch| bb_00B2FFE2
  bb_00B2FFE2 -->|fallthrough| bb_00B2FFEC
  bb_00B2FFEC -->|branch| bb_00B2FFDC
  bb_00B2FFEC -->|fallthrough| bb_00B2FFFD
```
