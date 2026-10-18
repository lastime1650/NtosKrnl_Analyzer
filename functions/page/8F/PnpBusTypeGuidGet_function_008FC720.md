# PnpBusTypeGuidGet

- RVA: `0x008FC720`–`0x008FC77B` (길이 `91` bytes)
- VA: `0x00000001408FC720`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006CF28`
- 디코드: `25`개 명령, `91/91` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x008FC737` → [ExAcquireFastMutex](../../text/20/ExAcquireFastMutex_function_0020E5A0.md) (function, `0x0020E5A0`)
- `0x008FC761` → [ExReleaseFastMutex](../../text/25/ExReleaseFastMutex_function_002519C0.md) (function, `0x002519C0`)

### Direct callers
- [IoGetDeviceProperty](IoGetDeviceProperty_function_008FA720.md) at `0x008FAAD7`

### Static image references
- `0x008FC730` → RVA `0x00F8CC00` (`.data`; read)
- `0x008FC73C` → RVA `0x00F8CB28` (`.data`; read)
- `0x008FC744` → RVA `0x00F8CB30` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x008FC737` → [ExAcquireFastMutex](../../text/20/ExAcquireFastMutex_function_0020E5A0.md) (`PAGE` → `.text`)
  - `0x008FC761` → [ExReleaseFastMutex](../../text/25/ExReleaseFastMutex_function_002519C0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
008FC720  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
008FC725  57                              push rdi
008FC726  48 83 EC 20                     sub rsp, 0x20
008FC72A  0F B7 D9                        movzx ebx, cx
008FC72D  48 8B FA                        mov rdi, rdx
008FC730  48 8D 0D C9 04 69 00            lea rcx, [rip + 0x6904c9]
008FC737  E8 64 1E 91 FF                  call 0x14020e5a0
008FC73C  3B 1D E6 03 69 00               cmp ebx, dword ptr [rip + 0x6903e6]
008FC742  73 30                           jae 0x1408fc774
008FC744  48 8B 05 E5 03 69 00            mov rax, qword ptr [rip + 0x6903e5]
008FC74B  8B CB                           mov ecx, ebx
008FC74D  48 03 C9                        add rcx, rcx
008FC750  33 DB                           xor ebx, ebx
008FC752  0F 10 04 C8                     movups xmm0, xmmword ptr [rax + rcx*8]
008FC756  F3 0F 7F 07                     movdqu xmmword ptr [rdi], xmm0
008FC75A  48 8D 0D 9F 04 69 00            lea rcx, [rip + 0x69049f]
008FC761  E8 5A 52 95 FF                  call 0x1402519c0
008FC766  8B C3                           mov eax, ebx
008FC768  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
008FC76D  48 83 C4 20                     add rsp, 0x20
008FC771  5F                              pop rdi
008FC772  C3                              ret
008FC773  CC                              int3
008FC774  BB 34 00 00 C0                  mov ebx, 0xc0000034
008FC779  EB DF                           jmp 0x1408fc75a
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PnpBusTypeGuidGet(unsigned __int16 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    result = ExAcquireFastMutex(v_rip + 6882505, a2, a3, a4);
    if (a1 >= (*(unsigned int *)(v_rip + 6882278))) goto loc_008FC774;
    a1 = ((unsigned int)(a1)) + ((unsigned int)(a1));
    v_rbx = 0;
    *(unsigned __int64 *)(a2) = v_xmm0;
loc_008FC75A:
    result = ExReleaseFastMutex(v_rip + 6882463, a2, a3, a4);
    v_rsp = (v_rsp) + (32);
    return 0;
loc_008FC774:
    goto loc_008FC75A;
}
```

## 5. (Beta) C Style

```c
int64_t PnpBusTypeGuidGet(uint16_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    result = ExAcquireFastMutex(v_rip + 6882505, Arg2, a3, a4);
    if (Arg1 >= (*(uint32_t *)(v_rip + 0x6903E6))) goto loc_008FC774;
    Arg1 = ((uint32_t)(Arg1)) + ((uint32_t)(Arg1));
    local_rbx = 0;
    *(uint64_t *)(arg2) = v_xmm0;
loc_008FC75A:
    result = ExReleaseFastMutex(v_rip + 6882463, Arg2, a3, a4);
    local_rsp = (local_rsp) + (32);
    return 0;
loc_008FC774:
    goto loc_008FC75A;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x0` | `128` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008FC720&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_008FC720[BB_008FC720]
  bb_008FC744[BB_008FC744]
  bb_008FC75A[BB_008FC75A]
  bb_008FC773[BB_008FC773]
  bb_008FC774[BB_008FC774]
  bb_008FC720 -->|branch| bb_008FC774
  bb_008FC720 -->|fallthrough| bb_008FC744
  bb_008FC744 -->|flow| bb_008FC75A
  bb_008FC773 -->|flow| bb_008FC774
  bb_008FC774 -->|branch| bb_008FC75A
```
