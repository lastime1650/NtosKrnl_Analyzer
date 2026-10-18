# HvlpFastSendSyntheticClusterIpiEx

- RVA: `0x00304F78`–`0x00305018` (길이 `160` bytes)
- VA: `0x0000000140304F78`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00073604`
- 디코드: `35`개 명령, `160/160` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00304FA3` → [HvlpAffinityToHvProcessorSet](HvlpAffinityToHvProcessorSet_function_003068F4.md) (function, `0x003068F4`)
- `0x00304FF0` → [HvcallFastExtended](../31/HvcallFastExtended_function_003130E0.md) (function, `0x003130E0`)
- `0x0030500A` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [HvlSendSyntheticClusterIpi](HvlSendSyntheticClusterIpi_function_00304E50.md) at `0x00304F25`

### Static image references
- `0x00304F7F` → RVA `0x00E0A740` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00304F78  48 81 EC C8 00 00 00            sub rsp, 0xc8
00304F7F  48 8B 05 BA 57 B0 00            mov rax, qword ptr [rip + 0xb057ba]
00304F86  48 33 C4                        xor rax, rsp
00304F89  48 89 84 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], rax
00304F91  8B C2                           mov eax, edx
00304F93  41 B8 58 00 00 00               mov r8d, 0x58
00304F99  48 8D 54 24 48                  lea rdx, [rsp + 0x48]
00304F9E  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00304FA3  E8 4C 19 00 00                  call 0x1403068f4
00304FA8  83 64 24 20 00                  and dword ptr [rsp + 0x20], 0
00304FAD  45 33 C9                        xor r9d, r9d
00304FB0  48 C7 44 24 30 15 00 00 00      mov qword ptr [rsp + 0x30], 0x15
00304FB9  8D 50 07                        lea edx, [rax + 7]
00304FBC  C1 E2 0E                        shl edx, 0xe
00304FBF  44 8D 40 18                     lea r8d, [rax + 0x18]
00304FC3  81 E2 00 00 FE 03               and edx, 0x3fe0000
00304FC9  8B CA                           mov ecx, edx
00304FCB  81 CA 15 00 01 00               or edx, 0x10015
00304FD1  83 C9 15                        or ecx, 0x15
00304FD4  89 4C 24 30                     mov dword ptr [rsp + 0x30], ecx
00304FD8  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
00304FDD  48 89 4C 24 30                  mov qword ptr [rsp + 0x30], rcx
00304FE2  89 54 24 30                     mov dword ptr [rsp + 0x30], edx
00304FE6  48 8D 54 24 40                  lea rdx, [rsp + 0x40]
00304FEB  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
00304FF0  E8 EB E0 00 00                  call 0x1403130e0
00304FF5  66 F7 D8                        neg ax
00304FF8  1B C0                           sbb eax, eax
00304FFA  25 01 00 00 C0                  and eax, 0xc0000001
00304FFF  48 8B 8C 24 B0 00 00 00         mov rcx, qword ptr [rsp + 0xb0]
00305007  48 33 CC                        xor rcx, rsp
0030500A  E8 31 76 3A 00                  call 0x1406ac640
0030500F  48 81 C4 C8 00 00 00            add rsp, 0xc8
00305016  C3                              ret
00305017  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HvlpFastSendSyntheticClusterIpiEx(__int64 a1, int a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m98;
    unsigned int v_stack_mA8;

    v_rsp = (v_rsp) - (200);
    result = (*(unsigned __int64 *)(v_rip + 11556794)) ^ (v_rsp);
    v_stack_m18 = result;
    v_stack_m88 = (unsigned int)(a2);
    result = HvlpAffinityToHvProcessorSet(a1, v_stack_m80, 88, a4);
    a4 = 0;
    v_stack_m98 = 21;
    a2 = (unsigned int)((result + 7) << (14));
    a2 = (unsigned int)((a2) & (0x3FE0000ULL));
    a2 = (unsigned int)((a2) | (0x10015ULL));
    a1 = (unsigned int)(((unsigned int)(a2)) | (21));
    v_stack_m98 = (unsigned int)(a1);
    v_stack_m98 = v_stack_m98;
    v_stack_m98 = a2;
    result = HvcallFastExtended(v_stack_m98, v_stack_m88, result + 24, a4);
    result = (unsigned __int16)(-(result));
    result = (unsigned int)((result) & (0xC0000001ULL));
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, v_stack_m88, result + 24, a4);
    v_rsp = (v_rsp) + (200);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t HvlpFastSendSyntheticClusterIpiEx(int64_t Arg1, int32_t Arg2, int64_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m98;
    uint32_t v_stack_mA8;

    local_rsp = (local_rsp) - (200);
    result = (*(uint64_t *)(v_rip + 0xB057BA)) ^ (local_rsp);
    v_stack_m18 = result;
    v_stack_m88 = (uint32_t)(Arg2);
    result = HvlpAffinityToHvProcessorSet(Arg1, v_stack_m80, 88, Arg4);
    Arg4 = 0;
    v_stack_m98 = 21;
    Arg2 = (uint32_t)((result + 7) << (14));
    Arg2 = (uint32_t)((Arg2) & (0x3FE0000ULL));
    Arg2 = (uint32_t)((Arg2) | (0x10015ULL));
    Arg1 = (uint32_t)(((uint32_t)(Arg2)) | (21));
    v_stack_m98 = (uint32_t)(Arg1);
    v_stack_m98 = v_stack_m98;
    v_stack_m98 = Arg2;
    result = HvcallFastExtended(v_stack_m98, v_stack_m88, result + 24, Arg4);
    result = (uint16_t)(-(result));
    result = (uint32_t)((result) & (0xC0000001ULL));
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, v_stack_m88, result + 24, Arg4);
    local_rsp = (local_rsp) + (200);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00304F78&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00304F78[BB_00304F78]
  bb_00305017[BB_00305017]
```
