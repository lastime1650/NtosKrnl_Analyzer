# HalpPmuArbiterQueryRegistryQuantum

- RVA: `0x00707D04`–`0x00707DAC` (길이 `168` bytes)
- VA: `0x0000000140707D04`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C3D54`
- 디코드: `40`개 명령, `168/168` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **4**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **5**

### Outgoing calls
- `0x00707D20` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00707D58` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00707D61` → [MmGetSystemRoutineAddress](../90/MmGetSystemRoutineAddress_function_0090EFE0.md) (function, `0x0090EFE0`)
- `0x00707D8C` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- [HalpHwPerfCntInitSystem](../../pagelk/B5/HalpHwPerfCntInitSystem_function_00B5C590.md) at `0x00B5C5BB`

### Static image references
- `0x00707D25` → RVA `0x00023D90` (`.rdata`; read)
- `0x00707D37` → RVA `0x00023C80` (`.rdata`; read)
- `0x00707D66` → RVA `0x008C8FD0` (`RtlQueryRegistryValues`; read)
- `0x00707D78` → RVA `0x00023DB8` (`.rdata`; read)
- `0x00707D9C` → RVA `0x00FC2BC0` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x00707D20` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00707D58` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x00707D8C` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00707D04  40 55                           push rbp
00707D06  48 8D 6C 24 A9                  lea rbp, [rsp - 0x57]
00707D0B  48 81 EC B0 00 00 00            sub rsp, 0xb0
00707D12  83 65 67 00                     and dword ptr [rbp + 0x67], 0
00707D16  48 8D 4D E7                     lea rcx, [rbp - 0x19]
00707D1A  33 D2                           xor edx, edx
00707D1C  44 8D 42 70                     lea r8d, [rdx + 0x70]
00707D20  E8 1B EF FB FF                  call 0x1406c6c40
00707D25  48 8D 05 64 C0 91 FF            lea rax, [rip - 0x6e3f9c]
00707D2C  C7 45 EF 20 01 00 00            mov dword ptr [rbp - 0x11], 0x120
00707D33  48 89 45 F7                     mov qword ptr [rbp - 9], rax
00707D37  48 8D 15 42 BF 91 FF            lea rdx, [rip - 0x6e40be]
00707D3E  48 8D 45 67                     lea rax, [rbp + 0x67]
00707D42  C7 45 07 00 00 00 04            mov dword ptr [rbp + 7], 0x4000000
00707D49  0F 57 C0                        xorps xmm0, xmm0
00707D4C  48 89 45 FF                     mov qword ptr [rbp - 1], rax
00707D50  48 8D 4D D7                     lea rcx, [rbp - 0x29]
00707D54  0F 11 45 D7                     movups xmmword ptr [rbp - 0x29], xmm0
00707D58  E8 23 2A D2 FF                  call 0x14042a780
00707D5D  48 8D 4D D7                     lea rcx, [rbp - 0x29]
00707D61  E8 7A 72 20 00                  call 0x14090efe0
00707D66  48 8D 0D 63 12 1C 00            lea rcx, [rip + 0x1c1263]
00707D6D  48 85 C0                        test rax, rax
00707D70  4C 8D 45 E7                     lea r8, [rbp - 0x19]
00707D74  48 0F 44 C1                     cmove rax, rcx
00707D78  48 8D 15 39 C0 91 FF            lea rdx, [rip - 0x6e3fc7]
00707D7F  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
00707D85  45 33 C9                        xor r9d, r9d
00707D88  41 8D 49 02                     lea ecx, [r9 + 2]
00707D8C  E8 3F 2D FB FF                  call 0x1406baad0
00707D91  85 C0                           test eax, eax
00707D93  78 0D                           js 0x140707da2
00707D95  8B 45 67                        mov eax, dword ptr [rbp + 0x67]
00707D98  85 C0                           test eax, eax
00707D9A  74 06                           je 0x140707da2
00707D9C  89 05 1E AE 8B 00               mov dword ptr [rip + 0x8bae1e], eax
00707DA2  48 81 C4 B0 00 00 00            add rsp, 0xb0
00707DA9  5D                              pop rbp
00707DAA  C3                              ret
00707DAB  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpPmuArbiterQueryRegistryQuantum(__int64 a1, int a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned int v_stack_m58;
    unsigned __int64 v_stack_m5F;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned int v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m98;
    unsigned int v_stack_p8;

    v_rsp = (v_rsp) - (176);
    a2 = 0;
    result = memset(v_stack_m78, a2, a2 + 112, a4);
    v_stack_m70 = 288;
    v_stack_m68 = v_rip - 7225244;
    v_stack_m58 = 0x4000000ULL;
    v_stack_m60 = v_stack_p8;
    v_stack_m88 = v_xmm0;
    result = RtlInitUnicodeString(v_stack_m88, v_rip - 7225534, a2 + 112, a4);
    result = MmGetSystemRoutineAddress(v_stack_m88, v_rip - 7225534, a2 + 112, a4);
    if (result == 0) { result = v_rip + 1839715; }
    a4 = 0;
    result = guard_dispatch_icall(a4 + 2, v_rip - 7225287, v_stack_m78, a4);
    if (sign_flag) goto loc_00707DA2;
    if ((unsigned int)((unsigned int)(v_stack_p8)) != 0) {
        *(unsigned int *)(v_rip + 9154078) = (unsigned int)((unsigned int)(v_stack_p8));
    }
    v_rsp = (v_rsp) + (176);
    return (unsigned int)(v_stack_p8);
}
```

## 5. (Beta) C Style

```c
int64_t HalpPmuArbiterQueryRegistryQuantum(int64_t Arg1, int32_t Arg2, int64_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rsp;
    uint32_t v_stack_m58;
    uint64_t v_stack_m5F;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint32_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m88;
    uint64_t v_stack_m98;
    uint32_t v_stack_p8;

    local_rsp = (local_rsp) - (176);
    Arg2 = 0;
    result = memset(v_stack_m78, Arg2, Arg2 + 112, Arg4);
    v_stack_m70 = 288;
    v_stack_m68 = v_rip - 7225244;
    v_stack_m58 = 0x4000000ULL;
    v_stack_m60 = v_stack_p8;
    v_stack_m88 = v_xmm0;
    result = RtlInitUnicodeString(v_stack_m88, v_rip - 7225534, Arg2 + 112, Arg4);
    result = MmGetSystemRoutineAddress(v_stack_m88, v_rip - 7225534, Arg2 + 112, Arg4);
    if (result == 0) { result = v_rip + 1839715; }
    Arg4 = 0;
    result = guard_dispatch_icall(Arg4 + 2, v_rip - 7225287, v_stack_m78, Arg4);
    if (sign_flag) goto loc_00707DA2;
    if ((uint32_t)((uint32_t)(v_stack_p8)) != 0) {
        *(uint32_t *)(v_rip + 0x8BAE1E) = (uint32_t)((uint32_t)(v_stack_p8));
    }
    local_rsp = (local_rsp) + (176);
    return (uint32_t)(v_stack_p8);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00707D04&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00707D04[BB_00707D04]
  bb_00707D95[BB_00707D95]
  bb_00707D9C[BB_00707D9C]
  bb_00707DA2[BB_00707DA2]
  bb_00707DAB[BB_00707DAB]
  bb_00707D04 -->|branch| bb_00707DA2
  bb_00707D04 -->|fallthrough| bb_00707D95
  bb_00707D95 -->|branch| bb_00707DA2
  bb_00707D95 -->|fallthrough| bb_00707D9C
  bb_00707D9C -->|flow| bb_00707DA2
```
