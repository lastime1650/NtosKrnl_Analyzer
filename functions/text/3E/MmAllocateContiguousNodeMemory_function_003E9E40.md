# MmAllocateContiguousNodeMemory

- RVA: `0x003E9E40`–`0x003E9EEF` (길이 `175` bytes)
- VA: `0x00000001403E9E40`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000958D8`
- 디코드: `37`개 명령, `175/175` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **11**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x003E9E8A` → [MiConvertContiguousMemoryParameters](MiConvertContiguousMemoryParameters_function_003E9EF8.md) (function, `0x003E9EF8`)
- `0x003E9ED0` → [MiAllocateContiguousMemory](MiAllocateContiguousMemory_function_003E9FDC.md) (function, `0x003E9FDC`)
- `0x003E9EDD` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [MmAllocateContiguousMemorySpecifyCacheNode](MmAllocateContiguousMemorySpecifyCacheNode_function_003E9D30.md) at `0x003E9D4E`
- [HalAllocateCommonBufferExV2](HalAllocateCommonBufferExV2_function_003E9DB0.md) at `0x003E9E0D`
- [HalpDmaAllocateContiguousMemory](HalpDmaAllocateContiguousMemory_function_003EBD0C.md) at `0x003EBD83`
- [HalpInterruptBuildGlobalStartupStub](../54/HalpInterruptBuildGlobalStartupStub_function_0054343C.md) at `0x00543495`
- [HalpDmaControllerInitializeController](../55/HalpDmaControllerInitializeController_function_00554198.md) at `0x00554210`
- [HalpAllocateCR3Root](../55/HalpAllocateCR3Root_function_0055A914.md) at `0x0055A94B`
- [HvlpAllocateOverlayPages](../58/HvlpAllocateOverlayPages_function_0058D3F8.md) at `0x0058D435`
- [HvlpAllocateOverlayPages](../58/HvlpAllocateOverlayPages_function_0058D3F8.md) at `0x0058D445`
- [IopInitializeInMemoryDumpData](../59/IopInitializeInMemoryDumpData_function_005957E0.md) at `0x005958E7`
- [DifMmAllocateContiguousNodeMemoryWrapper](../63/DifMmAllocateContiguousNodeMemoryWrapper_function_006340B0.md) at `0x006341C5`
- [ViAllocateContiguousMemory](../../pagevrfy/B9/ViAllocateContiguousMemory_function_00B97CE0.md) at `0x00B97D9B`
- [IommupHvInitializeLibrary](../../init/C2/IommupHvInitializeLibrary_function_00C25024.md) at `0x00C2512D`

### Static image references
- `0x003E9E4C` → RVA `0x00E0A740` (`.data`; read)
- `0x003E9E98` → RVA `0x00E38D00` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
003E9E40  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
003E9E45  48 81 EC 88 00 00 00            sub rsp, 0x88
003E9E4C  48 8B 05 ED 08 A2 00            mov rax, qword ptr [rip + 0xa208ed]
003E9E53  48 33 C4                        xor rax, rsp
003E9E56  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
003E9E5B  44 8B 9C 24 B8 00 00 00         mov r11d, dword ptr [rsp + 0xb8]
003E9E63  48 8D 44 24 50                  lea rax, [rsp + 0x50]
003E9E68  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
003E9E6D  0F 57 C0                        xorps xmm0, xmm0
003E9E70  8B 84 24 B0 00 00 00            mov eax, dword ptr [rsp + 0xb0]
003E9E77  44 89 5C 24 28                  mov dword ptr [rsp + 0x28], r11d
003E9E7C  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
003E9E80  0F 11 44 24 50                  movups xmmword ptr [rsp + 0x50], xmm0
003E9E85  0F 11 44 24 60                  movups xmmword ptr [rsp + 0x60], xmm0
003E9E8A  E8 69 00 00 00                  call 0x1403e9ef8
003E9E8F  85 C0                           test eax, eax
003E9E91  78 58                           js 0x1403e9eeb
003E9E93  83 64 24 40 00                  and dword ptr [rsp + 0x40], 0
003E9E98  48 8D 05 61 EE A4 00            lea rax, [rip + 0xa4ee61]
003E9E9F  4C 8B 4C 24 60                  mov r9, qword ptr [rsp + 0x60]
003E9EA4  48 8D 8C 24 90 00 00 00         lea rcx, [rsp + 0x90]
003E9EAC  4C 8B 44 24 58                  mov r8, qword ptr [rsp + 0x58]
003E9EB1  48 8B 54 24 50                  mov rdx, qword ptr [rsp + 0x50]
003E9EB6  C7 44 24 38 43 6F 6E 54         mov dword ptr [rsp + 0x38], 0x546e6f43
003E9EBE  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
003E9EC3  8B 44 24 68                     mov eax, dword ptr [rsp + 0x68]
003E9EC7  44 89 5C 24 28                  mov dword ptr [rsp + 0x28], r11d
003E9ECC  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
003E9ED0  E8 07 01 00 00                  call 0x1403e9fdc
003E9ED5  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
003E9EDA  48 33 CC                        xor rcx, rsp
003E9EDD  E8 5E 27 2C 00                  call 0x1406ac640
003E9EE2  48 81 C4 88 00 00 00            add rsp, 0x88
003E9EE9  C3                              ret
003E9EEA  CC                              int3
003E9EEB  33 C0                           xor eax, eax
003E9EED  EB E6                           jmp 0x1403e9ed5
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MmAllocateContiguousNodeMemory(__int64 a1, __int64 a2, __int64 a3, __int64 a4, unsigned int a5, unsigned int a6)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned int v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned int v_stack_m48;
    unsigned int v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned int v_stack_m60;
    unsigned int v_stack_m68;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (136);
    result = (*(unsigned __int64 *)(v_rip + 10619117)) ^ (v_rsp);
    v_stack_m18 = result;
    v_stack_m58 = v_stack_m38;
    v_stack_m60 = (unsigned int)((unsigned int)(a6));
    v_stack_m68 = (unsigned int)((unsigned int)(a5));
    v_stack_m38 = v_xmm0;
    v_stack_m28 = v_xmm0;
    result = MiConvertContiguousMemoryParameters(a1, a2, a3, a4);
    if (sign_flag) goto loc_003E9EEB;
    v_stack_m50 = 0x546E6F43ULL;
    v_stack_m58 = v_rip + 10808929;
    v_stack_m60 = (unsigned int)((unsigned int)(a6));
    v_stack_m68 = (unsigned int)((unsigned int)(v_stack_m20));
    result = MiAllocateContiguousMemory(v_stack_p8, v_stack_m38, v_stack_m30, v_stack_m28);
loc_003E9ED5:
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, v_stack_m38, v_stack_m30, v_stack_m28);
    v_rsp = (v_rsp) + (136);
    return result;
loc_003E9EEB:
    result = 0;
    goto loc_003E9ED5;
}
```

## 5. (Beta) C Style

```c
int64_t MmAllocateContiguousNodeMemory(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint32_t Arg5, uint32_t Arg6)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint32_t v_stack_m20;
    uint64_t v_stack_m28;
    uint64_t v_stack_m30;
    uint64_t v_stack_m38;
    uint32_t v_stack_m48;
    uint32_t v_stack_m50;
    uint64_t v_stack_m58;
    uint32_t v_stack_m60;
    uint32_t v_stack_m68;
    uint64_t v_stack_p8;

    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (136);
    result = (*(uint64_t *)(v_rip + 0xA208ED)) ^ (local_rsp);
    v_stack_m18 = result;
    v_stack_m58 = v_stack_m38;
    v_stack_m60 = (uint32_t)((uint32_t)(Arg6));
    v_stack_m68 = (uint32_t)((uint32_t)(Arg5));
    v_stack_m38 = v_xmm0;
    v_stack_m28 = v_xmm0;
    result = MiConvertContiguousMemoryParameters(Arg1, Arg2, Arg3, Arg4);
    if (sign_flag) goto loc_003E9EEB;
    v_stack_m50 = 0x546E6F43ULL;
    v_stack_m58 = v_rip + 10808929;
    v_stack_m60 = (uint32_t)((uint32_t)(Arg6));
    v_stack_m68 = (uint32_t)((uint32_t)(v_stack_m20));
    result = MiAllocateContiguousMemory(v_stack_p8, v_stack_m38, v_stack_m30, v_stack_m28);
loc_003E9ED5:
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, v_stack_m38, v_stack_m30, v_stack_m28);
    local_rsp = (local_rsp) + (136);
    return result;
loc_003E9EEB:
    result = 0;
    goto loc_003E9ED5;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003E9E40&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_003E9E40[BB_003E9E40]
  bb_003E9E93[BB_003E9E93]
  bb_003E9ED5[BB_003E9ED5]
  bb_003E9EEA[BB_003E9EEA]
  bb_003E9EEB[BB_003E9EEB]
  bb_003E9E40 -->|branch| bb_003E9EEB
  bb_003E9E40 -->|fallthrough| bb_003E9E93
  bb_003E9E93 -->|flow| bb_003E9ED5
  bb_003E9EEA -->|flow| bb_003E9EEB
  bb_003E9EEB -->|branch| bb_003E9ED5
```
