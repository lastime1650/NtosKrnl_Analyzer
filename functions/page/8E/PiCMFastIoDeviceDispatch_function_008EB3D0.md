# PiCMFastIoDeviceDispatch

- RVA: `0x008EB3D0`–`0x008EB438` (길이 `104` bytes)
- VA: `0x00000001408EB3D0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00086C28`
- 디코드: `28`개 명령, `104/104` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x008EB3E7` → [IoIs32bitProcess](../../text/40/IoIs32bitProcess_function_0040DFE0.md) (function, `0x0040DFE0`)
- `0x008EB41E` → [PiCMHandleIoctl](PiCMHandleIoctl_function_008EB880.md) (function, `0x008EB880`)

### Direct callers
- [IopXxxControlFile](IopXxxControlFile_function_008E9AD0.md) at `0x008EA1B9`
- [PiDaFastIoDispatch](PiDaFastIoDispatch_function_008EC5B0.md) at `0x008EC621`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x008EB3E7` → [IoIs32bitProcess](../../text/40/IoIs32bitProcess_function_0040DFE0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
008EB3D0  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
008EB3D5  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
008EB3DA  57                              push rdi
008EB3DB  48 83 EC 40                     sub rsp, 0x40
008EB3DF  33 C9                           xor ecx, ecx
008EB3E1  41 8B F9                        mov edi, r9d
008EB3E4  49 8B F0                        mov rsi, r8
008EB3E7  E8 F4 2B B2 FF                  call 0x14040dfe0
008EB3EC  48 8B 9C 24 88 00 00 00         mov rbx, qword ptr [rsp + 0x88]
008EB3F4  8B D7                           mov edx, edi
008EB3F6  44 8B 4C 24 78                  mov r9d, dword ptr [rsp + 0x78]
008EB3FB  4C 8B 44 24 70                  mov r8, qword ptr [rsp + 0x70]
008EB400  0F B6 C0                        movzx eax, al
008EB403  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
008EB407  48 8D 4B 08                     lea rcx, [rbx + 8]
008EB40B  8B 84 24 80 00 00 00            mov eax, dword ptr [rsp + 0x80]
008EB412  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
008EB416  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
008EB41B  48 8B CE                        mov rcx, rsi
008EB41E  E8 5D 04 00 00                  call 0x1408eb880
008EB423  48 8B 74 24 58                  mov rsi, qword ptr [rsp + 0x58]
008EB428  89 03                           mov dword ptr [rbx], eax
008EB42A  B0 01                           mov al, 1
008EB42C  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
008EB431  48 83 C4 40                     add rsp, 0x40
008EB435  5F                              pop rdi
008EB436  C3                              ret
008EB437  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PiCMFastIoDeviceDispatch(int a1, __int64 a2, __int64 a3, int a4, __int64 a5, unsigned int a6, unsigned int a7, __int64 a8)
{
    __int64 result;
    __int64 v_rsp;
    unsigned int v_stack_m18;
    unsigned int v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rsi;
    v_rsp = (v_rsp) - (64);
    a1 = 0;
    result = IoIs32bitProcess(a1, a2, a3, a4);
    v_stack_m18 = (unsigned int)((unsigned __int8)(result));
    v_stack_m20 = (unsigned int)((unsigned int)(a7));
    v_stack_m28 = a8 + 8;
    result = PiCMHandleIoctl(a3, (unsigned int)((unsigned int)((unsigned int)(a4))), a5, (unsigned int)(a6));
    *(unsigned int *)(a8) = (unsigned int)(result);
    v_rsp = (v_rsp) + (64);
    return 1;
}
```

## 5. (Beta) C Style

```c
int64_t PiCMFastIoDeviceDispatch(int32_t Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4, int64_t Arg5, uint32_t Arg6, uint32_t Arg7, void *Arg8)
{
    uint8_t *arg8 = (uint8_t *)Arg8;

    int64_t result;
    int64_t local_rsp;
    uint32_t v_stack_m18;
    uint32_t v_stack_m20;
    uint64_t v_stack_m28;
    uint64_t v_stack_p10;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rsi;
    local_rsp = (local_rsp) - (64);
    Arg1 = 0;
    result = IoIs32bitProcess(Arg1, Arg2, Arg3, Arg4);
    v_stack_m18 = (uint32_t)((uint8_t)(result));
    v_stack_m20 = (uint32_t)((uint32_t)(Arg7));
    v_stack_m28 = Arg8 + 8;
    result = PiCMHandleIoctl(Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg4))), Arg5, (uint32_t)(Arg6));
    *(uint32_t *)(arg8) = (uint32_t)(result);
    local_rsp = (local_rsp) + (64);
    return 1;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg8` | `+ 0x0` | `32` | `W` |
| `Arg8` | `+ 0x8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008EB3D0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_008EB3D0[BB_008EB3D0]
  bb_008EB437[BB_008EB437]
```
