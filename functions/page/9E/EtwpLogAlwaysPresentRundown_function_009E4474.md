# EtwpLogAlwaysPresentRundown

- RVA: `0x009E4474`–`0x009E44D8` (길이 `100` bytes)
- VA: `0x00000001409E4474`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0007BD98`
- 디코드: `27`개 명령, `100/100` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x009E44A6` → [EtwpLogKernelEvent](../../text/25/EtwpLogKernelEvent_function_0025CC00.md) (function, `0x0025CC00`)
- `0x009E44D1` → [EtwpLogKernelEvent](../../text/25/EtwpLogKernelEvent_function_0025CC00.md) (function, `0x0025CC00`)

### Direct callers
- [EtwpUpdateSelectedGroupMasks](../../text/49/EtwpUpdateSelectedGroupMasks_function_0049B114.md) at `0x0049B38A`
- [EtwpLogKernelTraceRundown](EtwpLogKernelTraceRundown_function_009E400C.md) at `0x009E405E`

### Static image references
- `0x009E447E` → RVA `0x00F475F8` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x009E44A6` → [EtwpLogKernelEvent](../../text/25/EtwpLogKernelEvent_function_0025CC00.md) (`PAGE` → `.text`)
  - `0x009E44D1` → [EtwpLogKernelEvent](../../text/25/EtwpLogKernelEvent_function_0025CC00.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
009E4474  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
009E4479  57                              push rdi
009E447A  48 83 EC 30                     sub rsp, 0x30
009E447E  80 3D 73 31 56 00 00            cmp byte ptr [rip + 0x563173], 0
009E4485  8B DA                           mov ebx, edx
009E4487  48 8B F9                        mov rdi, rcx
009E448A  75 2B                           jne 0x1409e44b7
009E448C  C7 44 24 28 02 18 50 00         mov dword ptr [rsp + 0x28], 0x501802
009E4494  45 33 C9                        xor r9d, r9d
009E4497  44 8B C3                        mov r8d, ebx
009E449A  66 C7 44 24 20 08 00            mov word ptr [rsp + 0x20], 8
009E44A1  48 8B D7                        mov rdx, rdi
009E44A4  33 C9                           xor ecx, ecx
009E44A6  E8 55 87 87 FF                  call 0x14025cc00
009E44AB  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
009E44B0  48 83 C4 30                     add rsp, 0x30
009E44B4  5F                              pop rdi
009E44B5  C3                              ret
009E44B6  CC                              int3
009E44B7  C7 44 24 28 02 18 50 00         mov dword ptr [rsp + 0x28], 0x501802
009E44BF  45 33 C9                        xor r9d, r9d
009E44C2  44 8B C3                        mov r8d, ebx
009E44C5  66 C7 44 24 20 3A 0F            mov word ptr [rsp + 0x20], 0xf3a
009E44CC  48 8B D7                        mov rdx, rdi
009E44CF  33 C9                           xor ecx, ecx
009E44D1  E8 2A 87 87 FF                  call 0x14025cc00
009E44D6  EB B4                           jmp 0x1409e448c
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall EtwpLogAlwaysPresentRundown(__int64 a1, int a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned int v_stack_m10;
    unsigned __int16 v_stack_m18;
    unsigned __int16 v_stack_p20;
    unsigned int v_stack_p28;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (48);
    if ((*(unsigned __int8 *)(v_rip + 5648755)) != 0) goto loc_009E44B7;
loc_009E448C:
    v_stack_m10 = 0x501802ULL;
    a4 = 0;
    v_stack_m18 = 8;
    a1 = 0;
    result = EtwpLogKernelEvent(a1, a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a4);
    v_rsp = (v_rsp) + (48);
    return result;
loc_009E44B7:
    v_stack_p28 = 0x501802ULL;
    a4 = 0;
    v_stack_p20 = 0xF3AULL;
    a1 = 0;
    result = EtwpLogKernelEvent(a1, 0, (unsigned int)((unsigned int)(v_stack_p8)), a4);
    goto loc_009E448C;
}
```

## 5. (Beta) C Style

```c
int64_t EtwpLogAlwaysPresentRundown(int64_t Arg1, int32_t Arg2, int64_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rsp;
    uint32_t v_stack_m10;
    uint16_t v_stack_m18;
    uint16_t v_stack_p20;
    uint32_t v_stack_p28;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (48);
    if ((*(uint8_t *)(v_rip + 0x563173)) != 0) goto loc_009E44B7;
loc_009E448C:
    v_stack_m10 = 0x501802ULL;
    Arg4 = 0;
    v_stack_m18 = 8;
    Arg1 = 0;
    result = EtwpLogKernelEvent(Arg1, Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg4);
    local_rsp = (local_rsp) + (48);
    return result;
loc_009E44B7:
    v_stack_p28 = 0x501802ULL;
    Arg4 = 0;
    v_stack_p20 = 0xF3AULL;
    Arg1 = 0;
    result = EtwpLogKernelEvent(Arg1, 0, (uint32_t)((uint32_t)(v_stack_p8)), Arg4);
    goto loc_009E448C;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009E4474&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_009E4474[BB_009E4474]
  bb_009E448C[BB_009E448C]
  bb_009E44B6[BB_009E44B6]
  bb_009E44B7[BB_009E44B7]
  bb_009E4474 -->|branch| bb_009E44B7
  bb_009E4474 -->|fallthrough| bb_009E448C
  bb_009E44B6 -->|flow| bb_009E44B7
  bb_009E44B7 -->|branch| bb_009E448C
```
