# sub_00B3DF8C

- RVA: `0x00B3DF8C`–`0x00B3DFA8` (길이 `28` bytes)
- VA: `0x0000000140B3DF8C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000B2808`
- 디코드: `6`개 명령, `28/28` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00B3DF96` → RVA `0x00F01DF0` (`.data`; read/write)
- `0x00B3DF9C` → RVA `0x00F01DE8` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x00B3DFA3` → [WdipSemReserveInstanceTableEntry + 0xA5](../A5/WdipSemReserveInstanceTableEntry_function_00A5DA08.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00B3DF8C  48 89 03                        mov qword ptr [rbx], rax
00B3DF8F  48 89 4B 08                     mov qword ptr [rbx + 8], rcx
00B3DF93  48 89 19                        mov qword ptr [rcx], rbx
00B3DF96  FF 05 54 3E 3C 00               inc dword ptr [rip + 0x3c3e54]
00B3DF9C  48 89 1D 45 3E 3C 00            mov qword ptr [rip + 0x3c3e45], rbx
00B3DFA3  E9 05 FB F1 FF                  jmp 0x140a5daad
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall sub_00B3DF8C(__int64 a1)
{
    *(unsigned __int64 *)(v_rbx) = result;
    *(unsigned __int64 *)(v_rbx + 8) = a1;
    *(unsigned __int64 *)(a1) = v_rbx;
    *(unsigned __int64 *)(v_rip + 3948101) = v_rbx;
}
```

## 5. (Beta) C Style

```c
void sub_00B3DF8C(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    *(uint64_t *)(local_rbx) = result;
    *(void **)(local_rbx + 0x8) = Arg1;
    *(uint64_t *)(arg1) = local_rbx;
    *(uint64_t *)(v_rip + 0x3C3E45) = local_rbx;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00B3DF8C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B3DF8C[BB_00B3DF8C]
```
