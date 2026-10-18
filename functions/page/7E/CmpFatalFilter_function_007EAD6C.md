# CmpFatalFilter

- RVA: `0x007EAD6C`–`0x007EAD8E` (길이 `34` bytes)
- VA: `0x00000001407EAD6C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000622F0`
- 디코드: `9`개 명령, `34/34` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x007EAD88` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)

### Direct callers
- [CmpQueryKeyName$filt$0](../B0/CmpQueryKeyName_filt_0_function_00B0EAC0.md) at `0x00B0EAC9`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x007EAD88` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007EAD6C  48 83 EC 38                     sub rsp, 0x38
007EAD70  48 8B 01                        mov rax, qword ptr [rcx]
007EAD73  BA 21 00 00 00                  mov edx, 0x21
007EAD78  4C 8B 49 08                     mov r9, qword ptr [rcx + 8]
007EAD7C  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
007EAD82  4C 63 00                        movsxd r8, dword ptr [rax]
007EAD85  8D 4A 30                        lea ecx, [rdx + 0x30]
007EAD88  E8 D3 28 D1 FF                  call 0x1404fd660
007EAD8D  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpFatalFilter(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;

    v_rsp = (v_rsp) - (56);
    result = KeBugCheckEx(33 + 48, 33, (int)(*(unsigned int *)(*(unsigned __int64 *)(a1))), *(unsigned __int64 *)(a1 + 8));
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t CmpFatalFilter(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;

    local_rsp = (local_rsp) - (56);
    result = KeBugCheckEx(33 + 48, 33, (int32_t)(*(uint32_t *)(*(uint64_t *)(arg1))), *(uint64_t *)(arg1 + 0x8));
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007EAD6C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_007EAD6C[BB_007EAD6C]
```
