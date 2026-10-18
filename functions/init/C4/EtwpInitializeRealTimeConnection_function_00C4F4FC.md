# EtwpInitializeRealTimeConnection

- RVA: `0x00C4F4FC`–`0x00C4F5CC` (길이 `208` bytes)
- VA: `0x0000000140C4F4FC`
- 실행 섹션: `INIT`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C43B4`
- 디코드: `44`개 명령, `208/208` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **4**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **7**

### Outgoing calls
- `0x00C4F531` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00C4F592` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00C4F5A9` → [ObCreateObjectType](../../page/70/ObCreateObjectType_function_00705230.md) (function, `0x00705230`)
- `0x00C4F5B5` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [EtwpInitialize](EtwpInitialize_function_00C4DBCC.md) at `0x00C4DD83`

### Static image references
- `0x00C4F50E` → RVA `0x00E0A740` (`.data`; read)
- `0x00C4F536` → RVA `0x00011360` (`.rdata`; read)
- `0x00C4F541` → RVA `0x00A49730` (`EtwpOpenRealTimeConnectionObject`; read)
- `0x00C4F54C` → RVA `0x00C7D9E0` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C4F553` → RVA `0x007C0BF0` (`EtwpCloseRealTimeConnectionObject`; read)
- `0x00C4F566` → RVA `0x00AB93F0` (`EtwpDeleteRealTimeConnectionObject`; read)
- `0x00C4F597` → RVA `0x00FC53B0` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **4**
  - `0x00C4F531` → [memset](../../text/6C/memset_function_006C6C40.md) (`INIT` → `.text`)
  - `0x00C4F592` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`INIT` → `.text`)
  - `0x00C4F5A9` → [ObCreateObjectType](../../page/70/ObCreateObjectType_function_00705230.md) (`INIT` → `PAGE`)
  - `0x00C4F5B5` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`INIT` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00C4F4FC  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00C4F501  55                              push rbp
00C4F502  48 8D 6C 24 A9                  lea rbp, [rsp - 0x57]
00C4F507  48 81 EC C0 00 00 00            sub rsp, 0xc0
00C4F50E  48 8B 05 2B B2 1B 00            mov rax, qword ptr [rip + 0x1bb22b]
00C4F515  48 33 C4                        xor rax, rsp
00C4F518  48 89 45 47                     mov qword ptr [rbp + 0x47], rax
00C4F51C  0F 57 C0                        xorps xmm0, xmm0
00C4F51F  48 8D 4D C7                     lea rcx, [rbp - 0x39]
00C4F523  BB 78 00 00 00                  mov ebx, 0x78
00C4F528  33 D2                           xor edx, edx
00C4F52A  44 8B C3                        mov r8d, ebx
00C4F52D  0F 11 45 B7                     movups xmmword ptr [rbp - 0x49], xmm0
00C4F531  E8 0A 77 A7 FF                  call 0x1406c6c40
00C4F536  0F 10 05 23 1E 3C FF            movups xmm0, xmmword ptr [rip - 0xc3e1dd]
00C4F53D  80 4D C9 18                     or byte ptr [rbp - 0x37], 0x18
00C4F541  48 8D 05 E8 A1 DF FF            lea rax, [rip - 0x205e18]
00C4F548  48 89 45 FF                     mov qword ptr [rbp - 1], rax
00C4F54C  48 8D 15 8D E4 02 00            lea rdx, [rip + 0x2e48d]
00C4F553  48 8D 05 96 16 B7 FF            lea rax, [rip - 0x48e96a]
00C4F55A  66 89 5D C7                     mov word ptr [rbp - 0x39], bx
00C4F55E  48 89 45 07                     mov qword ptr [rbp + 7], rax
00C4F562  48 8D 4D B7                     lea rcx, [rbp - 0x49]
00C4F566  48 8D 05 83 9E E6 FF            lea rax, [rip - 0x19617d]
00C4F56D  C7 45 CF 00 01 00 00            mov dword ptr [rbp - 0x31], 0x100
00C4F574  48 89 45 0F                     mov qword ptr [rbp + 0xf], rax
00C4F578  F3 0F 7F 45 D3                  movdqu xmmword ptr [rbp - 0x2d], xmm0
00C4F57D  C7 45 E3 00 04 00 00            mov dword ptr [rbp - 0x1d], 0x400
00C4F584  C7 45 EB 00 02 00 00            mov dword ptr [rbp - 0x15], 0x200
00C4F58B  C7 45 F3 A0 00 00 00            mov dword ptr [rbp - 0xd], 0xa0
00C4F592  E8 E9 B1 7D FF                  call 0x14042a780
00C4F597  4C 8D 0D 12 5E 37 00            lea r9, [rip + 0x375e12]
00C4F59E  45 33 C0                        xor r8d, r8d
00C4F5A1  48 8D 55 C7                     lea rdx, [rbp - 0x39]
00C4F5A5  48 8D 4D B7                     lea rcx, [rbp - 0x49]
00C4F5A9  E8 82 5C AB FF                  call 0x140705230
00C4F5AE  48 8B 4D 47                     mov rcx, qword ptr [rbp + 0x47]
00C4F5B2  48 33 CC                        xor rcx, rsp
00C4F5B5  E8 86 D0 A5 FF                  call 0x1406ac640
00C4F5BA  48 8B 9C 24 D0 00 00 00         mov rbx, qword ptr [rsp + 0xd0]
00C4F5C2  48 81 C4 C0 00 00 00            add rsp, 0xc0
00C4F5C9  5D                              pop rbp
00C4F5CA  C3                              ret
00C4F5CB  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall EtwpInitializeRealTimeConnection(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m5F;
    unsigned __int64 v_stack_m60;
    unsigned int v_stack_m6C;
    unsigned int v_stack_m74;
    unsigned int v_stack_m7C;
    unsigned __int64 v_stack_m8C;
    unsigned int v_stack_m90;
    unsigned __int8 v_stack_m96;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (192);
    result = (*(unsigned __int64 *)(v_rip + 1815083)) ^ (v_rsp);
    v_stack_m18 = result;
    a2 = 0;
    v_stack_mA8 = v_xmm0;
    result = memset(v_stack_m98, a2, 120, a4);
    v_stack_m60 = v_rip - 2121240;
    v_stack_m98 = 120;
    v_stack_m58 = v_rip - 4778346;
    v_stack_m90 = 256;
    v_stack_m50 = v_rip - 1663357;
    v_stack_m8C = v_xmm0;
    v_stack_m7C = 0x400ULL;
    v_stack_m74 = 512;
    v_stack_m6C = 160;
    result = RtlInitUnicodeString(v_stack_mA8, v_rip + 189581, 120, a4);
    a3 = 0;
    result = ObCreateObjectType(v_stack_mA8, v_stack_m98, a3, v_rip + 3628562);
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, v_stack_m98, a3, v_rip + 3628562);
    v_rsp = (v_rsp) + (192);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t EtwpInitializeRealTimeConnection(int64_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m5F;
    uint64_t v_stack_m60;
    uint32_t v_stack_m6C;
    uint32_t v_stack_m74;
    uint32_t v_stack_m7C;
    uint64_t v_stack_m8C;
    uint32_t v_stack_m90;
    uint8_t v_stack_m96;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA8;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (192);
    result = (*(uint64_t *)(v_rip + 0x1BB22B)) ^ (local_rsp);
    v_stack_m18 = result;
    Arg2 = 0;
    v_stack_mA8 = v_xmm0;
    result = memset(v_stack_m98, Arg2, 120, a4);
    v_stack_m60 = v_rip - 2121240;
    v_stack_m98 = 120;
    v_stack_m58 = v_rip - 4778346;
    v_stack_m90 = 256;
    v_stack_m50 = v_rip - 1663357;
    v_stack_m8C = v_xmm0;
    v_stack_m7C = 0x400ULL;
    v_stack_m74 = 512;
    v_stack_m6C = 160;
    result = RtlInitUnicodeString(v_stack_mA8, v_rip + 189581, 120, a4);
    a3 = 0;
    result = ObCreateObjectType(v_stack_mA8, v_stack_m98, a3, v_rip + 3628562);
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, v_stack_m98, a3, v_rip + 3628562);
    local_rsp = (local_rsp) + (192);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=init&rva=0x00C4F4FC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00C4F4FC[BB_00C4F4FC]
  bb_00C4F5CB[BB_00C4F5CB]
```
