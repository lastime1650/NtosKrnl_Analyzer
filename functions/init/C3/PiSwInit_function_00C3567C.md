# PiSwInit

- RVA: `0x00C3567C`–`0x00C3577C` (길이 `256` bytes)
- VA: `0x0000000140C3567C`
- 실행 섹션: `INIT`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000794E0`
- 디코드: `49`개 명령, `256/256` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **4**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **22**

### Outgoing calls
- `0x00C356A0` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00C356EE` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00C3573D` → [ExInitializeResourceLite2](../../text/41/ExInitializeResourceLite2_function_0041F710.md) (function, `0x0041F710`)
- `0x00C35766` → [IoCreateDriver](../../page/AC/IoCreateDriver_function_00AC9D70.md) (function, `0x00AC9D70`)

### Direct callers
- [IopInitializePlugPlayServices](../C2/IopInitializePlugPlayServices_function_00C2F298.md) at `0x00C2FE3A`

### Static image references
- `0x00C35690` → RVA `0x00F8AAA0` (`.data`; read)
- `0x00C356A5` → RVA `0x00F8AB00` (`.data`; read/write)
- `0x00C356AD` → RVA `0x00A7E5C0` (`PiSwDeviceCompareObjects`; read)
- `0x00C356B6` → RVA `0x00F8AAA0` (`.data`; write)
- `0x00C356BD` → RVA `0x00F8ABA0` (`.data`; read)
- `0x00C356C4` → RVA `0x00F8AAE8` (`.data`; write)
- `0x00C356CB` → RVA `0x00AB3CA0` (`PiSwAllocateGenericTableEntry`; read)
- `0x00C356D5` → RVA `0x0073ABF0` (`PiSwFreeGenericTableEntry`; read)
- `0x00C356DC` → RVA `0x00F8AAF0` (`.data`; write)
- `0x00C356E7` → RVA `0x00F8AAF8` (`.data`; write)
- `0x00C356F3` → RVA `0x00F8AC00` (`.data`; read/write)
- `0x00C356FB` → RVA `0x00972590` (`PiSwBusRelationsCompareInstancePath`; read)
- `0x00C35702` → RVA `0x00F8ABE8` (`.data`; write)
- `0x00C35709` → RVA `0x00F8AB20` (`.data`; read)
- `0x00C35710` → RVA `0x00F8AB90` (`.data`; read)
- `0x00C35717` → RVA `0x00F8ABA0` (`.data`; write)
- `0x00C35721` → RVA `0x00F8AB98` (`.data`; write)
- `0x00C35728` → RVA `0x00F8AB90` (`.data`; write)
- `0x00C3572F` → RVA `0x00F8ABF0` (`.data`; write)
- `0x00C35736` → RVA `0x00F8ABF8` (`.data`; write)
- `0x00C35746` → RVA `0x00C7B000` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C35755` → RVA `0x00C35790` (`PiSwPdoDriverEntry`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **4**
  - `0x00C356A0` → [memset](../../text/6C/memset_function_006C6C40.md) (`INIT` → `.text`)
  - `0x00C356EE` → [memset](../../text/6C/memset_function_006C6C40.md) (`INIT` → `.text`)
  - `0x00C3573D` → [ExInitializeResourceLite2](../../text/41/ExInitializeResourceLite2_function_0041F710.md) (`INIT` → `.text`)
  - `0x00C35766` → [IoCreateDriver](../../page/AC/IoCreateDriver_function_00AC9D70.md) (`INIT` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00C3567C  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00C35681  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
00C35686  57                              push rdi
00C35687  48 83 EC 30                     sub rsp, 0x30
00C3568B  83 64 24 24 00                  and dword ptr [rsp + 0x24], 0
00C35690  48 8D 1D 09 54 35 00            lea rbx, [rip + 0x355409]
00C35697  33 D2                           xor edx, edx
00C35699  48 8B CB                        mov rcx, rbx
00C3569C  44 8D 42 68                     lea r8d, [rdx + 0x68]
00C356A0  E8 9B 15 A9 FF                  call 0x1406c6c40
00C356A5  48 83 25 53 54 35 00 00         and qword ptr [rip + 0x355453], 0
00C356AD  48 8D 05 0C 8F E4 FF            lea rax, [rip - 0x1b70f4]
00C356B4  33 D2                           xor edx, edx
00C356B6  48 89 1D E3 53 35 00            mov qword ptr [rip + 0x3553e3], rbx
00C356BD  48 8D 1D DC 54 35 00            lea rbx, [rip + 0x3554dc]
00C356C4  48 89 05 1D 54 35 00            mov qword ptr [rip + 0x35541d], rax
00C356CB  48 8D 35 CE E5 E7 FF            lea rsi, [rip - 0x181a32]
00C356D2  48 8B CB                        mov rcx, rbx
00C356D5  48 8D 3D 14 55 B0 FF            lea rdi, [rip - 0x4faaec]
00C356DC  48 89 35 0D 54 35 00            mov qword ptr [rip + 0x35540d], rsi
00C356E3  44 8D 42 68                     lea r8d, [rdx + 0x68]
00C356E7  48 89 3D 0A 54 35 00            mov qword ptr [rip + 0x35540a], rdi
00C356EE  E8 4D 15 A9 FF                  call 0x1406c6c40
00C356F3  48 83 25 05 55 35 00 00         and qword ptr [rip + 0x355505], 0
00C356FB  48 8D 05 8E CE D3 FF            lea rax, [rip - 0x2c3172]
00C35702  48 89 05 DF 54 35 00            mov qword ptr [rip + 0x3554df], rax
00C35709  48 8D 0D 10 54 35 00            lea rcx, [rip + 0x355410]
00C35710  48 8D 05 79 54 35 00            lea rax, [rip + 0x355479]
00C35717  48 89 1D 82 54 35 00            mov qword ptr [rip + 0x355482], rbx
00C3571E  83 CA FF                        or edx, 0xffffffff
00C35721  48 89 05 70 54 35 00            mov qword ptr [rip + 0x355470], rax
00C35728  48 89 05 61 54 35 00            mov qword ptr [rip + 0x355461], rax
00C3572F  48 89 35 BA 54 35 00            mov qword ptr [rip + 0x3554ba], rsi
00C35736  48 89 3D BB 54 35 00            mov qword ptr [rip + 0x3554bb], rdi
00C3573D  E8 CE 9F 7E FF                  call 0x14041f710
00C35742  85 C0                           test eax, eax
00C35744  78 25                           js 0x140c3576b
00C35746  48 8D 05 B3 58 04 00            lea rax, [rip + 0x458b3]
00C3574D  C7 44 24 20 2C 00 2E 00         mov dword ptr [rsp + 0x20], 0x2e002c
00C35755  48 8D 15 34 00 00 00            lea rdx, [rip + 0x34]
00C3575C  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00C35761  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00C35766  E8 05 46 E9 FF                  call 0x140ac9d70
00C3576B  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
00C35770  48 8B 74 24 48                  mov rsi, qword ptr [rsp + 0x48]
00C35775  48 83 C4 30                     add rsp, 0x30
00C35779  5F                              pop rdi
00C3577A  C3                              ret
00C3577B  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PiSwInit(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m10;
    unsigned int v_stack_m14;
    unsigned int v_stack_m18;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rsi;
    v_rsp = (v_rsp) - (48);
    a2 = 0;
    result = memset(v_rip + 3494921, a2, a2 + 104, a4);
    a2 = 0;
    *(unsigned __int64 *)(v_rip + 3494883) = v_rip + 3494921;
    *(unsigned __int64 *)(v_rip + 3494941) = v_rip - 1798388;
    *(unsigned __int64 *)(v_rip + 3494925) = v_rip - 1579570;
    *(unsigned __int64 *)(v_rip + 3494922) = v_rip - 5221100;
    result = memset(v_rip + 3495132, a2, a2 + 104, a4);
    *(unsigned __int64 *)(v_rip + 3495135) = v_rip - 2896242;
    *(unsigned __int64 *)(v_rip + 3495042) = v_rip + 3495132;
    a2 = (unsigned int)((a2) | (0xFFFFFFFFULL));
    *(unsigned __int64 *)(v_rip + 3495024) = v_rip + 3495033;
    *(unsigned __int64 *)(v_rip + 3495009) = v_rip + 3495033;
    *(unsigned __int64 *)(v_rip + 3495098) = v_rip - 1579570;
    *(unsigned __int64 *)(v_rip + 3495099) = v_rip - 5221100;
    result = ExInitializeResourceLite2(v_rip + 3494928, a2, a2 + 104, a4);
    if (!(sign_flag)) {
        result = v_rip + 284851;
        v_stack_m18 = 0x2E002CULL;
        a2 = v_rip + 52;
        v_stack_m10 = result;
        a1 = v_stack_m18;
        result = IoCreateDriver(a1, a2, a2 + 104, a4);
    }
    v_rsp = (v_rsp) + (48);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PiSwInit(int64_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m10;
    uint32_t v_stack_m14;
    uint32_t v_stack_m18;
    uint64_t v_stack_p10;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rsi;
    local_rsp = (local_rsp) - (48);
    Arg2 = 0;
    result = memset(v_rip + 3494921, Arg2, Arg2 + 104, a4);
    Arg2 = 0;
    *(uint64_t *)(v_rip + 0x3553E3) = v_rip + 3494921;
    *(uint64_t *)(v_rip + 0x35541D) = v_rip - 1798388;
    *(uint64_t *)(v_rip + 0x35540D) = v_rip - 1579570;
    *(uint64_t *)(v_rip + 0x35540A) = v_rip - 5221100;
    result = memset(v_rip + 3495132, Arg2, Arg2 + 104, a4);
    *(uint64_t *)(v_rip + 0x3554DF) = v_rip - 2896242;
    *(uint64_t *)(v_rip + 0x355482) = v_rip + 3495132;
    Arg2 = (uint32_t)((Arg2) | (0xFFFFFFFFULL));
    *(uint64_t *)(v_rip + 0x355470) = v_rip + 3495033;
    *(uint64_t *)(v_rip + 0x355461) = v_rip + 3495033;
    *(uint64_t *)(v_rip + 0x3554BA) = v_rip - 1579570;
    *(uint64_t *)(v_rip + 0x3554BB) = v_rip - 5221100;
    result = ExInitializeResourceLite2(v_rip + 3494928, Arg2, Arg2 + 104, a4);
    if (!(sign_flag)) {
        result = v_rip + 284851;
        v_stack_m18 = 0x2E002CULL;
        Arg2 = v_rip + 52;
        v_stack_m10 = result;
        Arg1 = v_stack_m18;
        result = IoCreateDriver(Arg1, Arg2, Arg2 + 104, a4);
    }
    local_rsp = (local_rsp) + (48);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=init&rva=0x00C3567C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00C3567C[BB_00C3567C]
  bb_00C35746[BB_00C35746]
  bb_00C3576B[BB_00C3576B]
  bb_00C3577B[BB_00C3577B]
  bb_00C3567C -->|branch| bb_00C3576B
  bb_00C3567C -->|fallthrough| bb_00C35746
  bb_00C35746 -->|flow| bb_00C3576B
```
