# VfMiscKeAcquireInStackQueuedSpinLockForDpc_Entry

- RVA: `0x00BADC60`–`0x00BADC92` (길이 `50` bytes)
- VA: `0x0000000140BADC60`
- 실행 섹션: `PAGEVRFY`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `15`개 명령, `50/50` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00BADC75` → [VfMiscCheckKernelAddress](../../text/4B/VfMiscCheckKernelAddress_function_004BC694.md) (function, `0x004BC694`)
- `0x00BADC86` → [VfMiscCheckKernelAddress](../../text/4B/VfMiscCheckKernelAddress_function_004BC694.md) (function, `0x004BC694`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x00BADC75` → [VfMiscCheckKernelAddress](../../text/4B/VfMiscCheckKernelAddress_function_004BC694.md) (`PAGEVRFY` → `.text`)
  - `0x00BADC86` → [VfMiscCheckKernelAddress](../../text/4B/VfMiscCheckKernelAddress_function_004BC694.md) (`PAGEVRFY` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00BADC60  40 53                           push rbx
00BADC62  48 83 EC 20                     sub rsp, 0x20
00BADC66  4C 8B 01                        mov r8, qword ptr [rcx]
00BADC69  48 8B D9                        mov rbx, rcx
00BADC6C  48 8B 49 10                     mov rcx, qword ptr [rcx + 0x10]
00BADC70  BA 08 00 00 00                  mov edx, 8
00BADC75  E8 1A EA 90 FF                  call 0x1404bc694
00BADC7A  4C 8B 03                        mov r8, qword ptr [rbx]
00BADC7D  BA 18 00 00 00                  mov edx, 0x18
00BADC82  48 8B 4B 08                     mov rcx, qword ptr [rbx + 8]
00BADC86  E8 09 EA 90 FF                  call 0x1404bc694
00BADC8B  48 83 C4 20                     add rsp, 0x20
00BADC8F  5B                              pop rbx
00BADC90  C3                              ret
00BADC91  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall VfMiscKeAcquireInStackQueuedSpinLockForDpc_Entry(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    result = VfMiscCheckKernelAddress(*(unsigned __int64 *)(a1 + 16), 8, *(unsigned __int64 *)(a1), a4);
    result = VfMiscCheckKernelAddress(*(unsigned __int64 *)(a1 + 8), 24, *(unsigned __int64 *)(a1), a4);
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t VfMiscKeAcquireInStackQueuedSpinLockForDpc_Entry(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    result = VfMiscCheckKernelAddress(*(uint64_t *)(arg1 + 0x10), 8, *(uint64_t *)(arg1), a4);
    result = VfMiscCheckKernelAddress(*(uint64_t *)(arg1 + 0x8), 24, *(uint64_t *)(arg1), a4);
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x10` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagevrfy&rva=0x00BADC60&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00BADC60[BB_00BADC60]
  bb_00BADC91[BB_00BADC91]
```
