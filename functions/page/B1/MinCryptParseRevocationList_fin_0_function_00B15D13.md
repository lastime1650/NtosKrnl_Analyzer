# MinCryptParseRevocationList$fin$0

- RVA: `0x00B15D13`–`0x00B15D4A` (길이 `55` bytes)
- VA: `0x0000000140B15D13`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000BF6EC`
- 디코드: `19`개 명령, `55/55` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00B15D3D` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00B15D3D` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00B15D13  40 55                           push rbp
00B15D15  48 83 EC 20                     sub rsp, 0x20
00B15D19  48 8B EA                        mov rbp, rdx
00B15D1C  0F B6 C1                        movzx eax, cl
00B15D1F  8B 4D 20                        mov ecx, dword ptr [rbp + 0x20]
00B15D22  BA E8 00 00 C0                  mov edx, 0xc00000e8
00B15D27  85 C0                           test eax, eax
00B15D29  0F 45 CA                        cmovne ecx, edx
00B15D2C  89 4D 20                        mov dword ptr [rbp + 0x20], ecx
00B15D2F  48 8B 4D 38                     mov rcx, qword ptr [rbp + 0x38]
00B15D33  48 85 C9                        test rcx, rcx
00B15D36  74 0B                           je 0x140b15d43
00B15D38  BA 43 49 63 72                  mov edx, 0x72634943
00B15D3D  E8 2E CB 06 00                  call 0x140b82870
00B15D42  90                              nop
00B15D43  48 83 C4 20                     add rsp, 0x20
00B15D47  5D                              pop rbp
00B15D48  C3                              ret
00B15D49  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MinCryptParseRevocationList_fin_0(unsigned __int8 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    a1 = (unsigned int)(*(unsigned int *)(a2 + 32));
    if (a1 != 0) { a1 = (unsigned int)((unsigned int)(0xC00000E8ULL)); }
    *(unsigned int *)(a2 + 32) = a1;
    result = a1;
    if (*(unsigned __int64 *)(a2 + 56) != 0) {
        a2 = 0x72634943ULL;
        result = ExFreePoolWithTag(*(unsigned __int64 *)(a2 + 56), a2, a3, a4);
    }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MinCryptParseRevocationList_fin_0(uint8_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    Arg1 = (uint32_t)(*(uint32_t *)(arg2 + 0x20));
    if (Arg1 != 0) { Arg1 = (uint32_t)((uint32_t)(0xC00000E8ULL)); }
    *(uint32_t *)(arg2 + 0x20) = Arg1;
    result = Arg1;
    if (*(uint64_t *)(arg2 + 0x38) != 0) {
        Arg2 = 0x72634943ULL;
        result = ExFreePoolWithTag(*(uint64_t *)(arg2 + 0x38), Arg2, a3, a4);
    }
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x20` | `32` | `R` |
| `Arg2` | `+ 0x20` | `32` | `W` |
| `Arg2` | `+ 0x38` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00B15D13&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B15D13[BB_00B15D13]
  bb_00B15D38[BB_00B15D38]
  bb_00B15D43[BB_00B15D43]
  bb_00B15D49[BB_00B15D49]
  bb_00B15D13 -->|branch| bb_00B15D43
  bb_00B15D13 -->|fallthrough| bb_00B15D38
  bb_00B15D38 -->|flow| bb_00B15D43
```
