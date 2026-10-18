# PopDiagTraceCsDripsDivergence

- RVA: `0x005D5F40`–`0x005D6026` (길이 `230` bytes)
- VA: `0x00000001405D5F40`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000CC830`
- 디코드: `54`개 명령, `230/230` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **5**

### Outgoing calls
- `0x005D5F8C` → [EtwEventEnabled](../39/EtwEventEnabled_function_00392450.md) (function, `0x00392450`)
- `0x005D600B` → [EtwWriteEx](../25/EtwWriteEx_function_0025F0D0.md) (function, `0x0025F0D0`)
- `0x005D6017` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [PopDripsWatchdogDiagnosticWorker](../../page/76/PopDripsWatchdogDiagnosticWorker_function_0076C600.md) at `0x0076C7A5`

### Static image references
- `0x005D5F5A` → RVA `0x00E0A740` (`.data`; read)
- `0x005D5F68` → RVA `0x00E67858` (`.data`; read)
- `0x005D5F6F` → RVA `0x00FC5270` (`ALMOSTRO`; read)
- `0x005D5F7E` → RVA `0x00F0B408` (`.data`; read)
- `0x005D5F85` → RVA `0x00020D00` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005D5F40  48 8B C4                        mov rax, rsp
005D5F43  4C 89 40 18                     mov qword ptr [rax + 0x18], r8
005D5F47  48 89 50 10                     mov qword ptr [rax + 0x10], rdx
005D5F4B  89 48 08                        mov dword ptr [rax + 8], ecx
005D5F4E  55                              push rbp
005D5F4F  48 8D 68 A1                     lea rbp, [rax - 0x5f]
005D5F53  48 81 EC A0 00 00 00            sub rsp, 0xa0
005D5F5A  48 8B 05 DF 47 83 00            mov rax, qword ptr [rip + 0x8347df]
005D5F61  48 33 C4                        xor rax, rsp
005D5F64  48 89 45 47                     mov qword ptr [rbp + 0x47], rax
005D5F68  80 3D E9 18 89 00 00            cmp byte ptr [rip + 0x8918e9], 0
005D5F6F  8B 05 FB F2 9E 00               mov eax, dword ptr [rip + 0x9ef2fb]
005D5F75  89 45 F7                        mov dword ptr [rbp - 9], eax
005D5F78  0F 84 92 00 00 00               je 0x1405d6010
005D5F7E  48 8B 0D 83 54 93 00            mov rcx, qword ptr [rip + 0x935483]
005D5F85  48 8D 15 74 AD A4 FF            lea rdx, [rip - 0x5b528c]
005D5F8C  E8 BF C4 DB FF                  call 0x140392450
005D5F91  84 C0                           test al, al
005D5F93  74 7B                           je 0x1405d6010
005D5F95  83 65 13 00                     and dword ptr [rbp + 0x13], 0
005D5F99  48 8D 45 67                     lea rax, [rbp + 0x67]
005D5F9D  83 65 23 00                     and dword ptr [rbp + 0x23], 0
005D5FA1  48 8D 15 58 AD A4 FF            lea rdx, [rip - 0x5b52a8]
005D5FA8  83 65 33 00                     and dword ptr [rbp + 0x33], 0
005D5FAC  41 B8 04 00 00 00               mov r8d, 4
005D5FB2  83 65 43 00                     and dword ptr [rbp + 0x43], 0
005D5FB6  45 33 C9                        xor r9d, r9d
005D5FB9  48 89 45 07                     mov qword ptr [rbp + 7], rax
005D5FBD  48 8D 45 6F                     lea rax, [rbp + 0x6f]
005D5FC1  48 89 45 17                     mov qword ptr [rbp + 0x17], rax
005D5FC5  48 8D 45 77                     lea rax, [rbp + 0x77]
005D5FC9  41 8D 48 04                     lea ecx, [r8 + 4]
005D5FCD  48 89 45 27                     mov qword ptr [rbp + 0x27], rax
005D5FD1  48 8D 45 F7                     lea rax, [rbp - 9]
005D5FD5  44 89 45 0F                     mov dword ptr [rbp + 0xf], r8d
005D5FD9  48 89 45 37                     mov qword ptr [rbp + 0x37], rax
005D5FDD  48 8D 45 07                     lea rax, [rbp + 7]
005D5FE1  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
005D5FE6  44 89 44 24 30                  mov dword ptr [rsp + 0x30], r8d
005D5FEB  48 83 64 24 28 00               and qword ptr [rsp + 0x28], 0
005D5FF1  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
005D5FF7  89 4D 1F                        mov dword ptr [rbp + 0x1f], ecx
005D5FFA  89 4D 2F                        mov dword ptr [rbp + 0x2f], ecx
005D5FFD  48 8B 0D 04 54 93 00            mov rcx, qword ptr [rip + 0x935404]
005D6004  44 89 45 3F                     mov dword ptr [rbp + 0x3f], r8d
005D6008  45 33 C0                        xor r8d, r8d
005D600B  E8 C0 90 C8 FF                  call 0x14025f0d0
005D6010  48 8B 4D 47                     mov rcx, qword ptr [rbp + 0x47]
005D6014  48 33 CC                        xor rcx, rsp
005D6017  E8 24 66 0D 00                  call 0x1406ac640
005D601C  48 81 C4 A0 00 00 00            add rsp, 0xa0
005D6023  5D                              pop rbp
005D6024  C3                              ret
005D6025  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopDiagTraceCsDripsDivergence(int a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m70;
    unsigned int v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;

    *(unsigned __int64 *)(v_rsp + 24) = a3;
    *(unsigned __int64 *)(v_rsp + 16) = a2;
    *(unsigned int *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (160);
    result = (*(unsigned __int64 *)(v_rip + 8603615)) ^ (v_rsp);
    *(unsigned __int64 *)(v_rsp - 95 + 71) = result;
    *(unsigned int *)(v_rsp - 95 - 9) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 10416891)));
    if ((*(unsigned __int8 *)(v_rip + 8984809)) == 0) goto loc_005D6010;
    result = EtwEventEnabled(*(unsigned __int64 *)(v_rip + 9655427), v_rip - 5984908, a3, a4);
    if ((unsigned __int8)(result) != 0) {
        result = v_rsp - 95 + 103;
        a2 = v_rip - 5984936;
        a3 = 4;
        a4 = 0;
        *(unsigned __int64 *)(v_rsp - 95 + 7) = result;
        result = v_rsp - 95 + 111;
        *(unsigned __int64 *)(v_rsp - 95 + 23) = result;
        result = v_rsp - 95 + 119;
        a1 = a3 + 4;
        *(unsigned __int64 *)(v_rsp - 95 + 39) = result;
        result = v_rsp - 95 - 9;
        *(unsigned int *)(v_rsp - 95 + 15) = (unsigned int)(a3);
        *(unsigned __int64 *)(v_rsp - 95 + 55) = result;
        result = v_rsp - 95 + 7;
        v_stack_m70 = result;
        v_stack_m78 = (unsigned int)(a3);
        *(unsigned int *)(v_rsp - 95 + 31) = a1;
        *(unsigned int *)(v_rsp - 95 + 47) = a1;
        a1 = *(unsigned __int64 *)(v_rip + 9655300);
        *(unsigned int *)(v_rsp - 95 + 63) = (unsigned int)(a3);
        a3 = 0;
        result = EtwWriteEx(a1, a2, a3, a4);
    }
    a1 = (*(unsigned __int64 *)(v_rsp - 95 + 71)) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (160);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PopDiagTraceCsDripsDivergence(int32_t Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m70;
    uint32_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;

    *(uint64_t *)(local_rsp + 0x18) = Arg3;
    *(uint64_t *)(local_rsp + 0x10) = Arg2;
    *(uint32_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (160);
    result = (*(uint64_t *)(v_rip + 0x8347DF)) ^ (local_rsp);
    *(uint64_t *)(local_rsp - 0x5F + 0x47) = result;
    *(uint32_t *)(local_rsp - 0x5F - 0x9) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x9EF2FB)));
    if ((*(uint8_t *)(v_rip + 0x8918E9)) == 0) goto loc_005D6010;
    result = EtwEventEnabled(*(uint64_t *)(v_rip + 0x935483), v_rip - 5984908, Arg3, Arg4);
    if ((uint8_t)(result) != 0) {
        result = local_rsp - 95 + 103;
        Arg2 = v_rip - 5984936;
        Arg3 = 4;
        Arg4 = 0;
        *(uint64_t *)(local_rsp - 0x5F + 0x7) = result;
        result = local_rsp - 95 + 111;
        *(uint64_t *)(local_rsp - 0x5F + 0x17) = result;
        result = local_rsp - 95 + 119;
        Arg1 = Arg3 + 4;
        *(uint64_t *)(local_rsp - 0x5F + 0x27) = result;
        result = local_rsp - 95 - 9;
        *(uint32_t *)(local_rsp - 0x5F + 0xF) = (uint32_t)(Arg3);
        *(uint64_t *)(local_rsp - 0x5F + 0x37) = result;
        result = local_rsp - 95 + 7;
        v_stack_m70 = result;
        v_stack_m78 = (uint32_t)(Arg3);
        *(uint32_t *)(local_rsp - 0x5F + 0x1F) = Arg1;
        *(uint32_t *)(local_rsp - 0x5F + 0x2F) = Arg1;
        Arg1 = *(uint64_t *)(v_rip + 0x935404);
        *(uint32_t *)(local_rsp - 0x5F + 0x3F) = (uint32_t)(Arg3);
        Arg3 = 0;
        result = EtwWriteEx(Arg1, Arg2, Arg3, Arg4);
    }
    Arg1 = (*(uint64_t *)(local_rsp - 0x5F + 0x47)) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (160);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005D5F40&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005D5F40[BB_005D5F40]
  bb_005D5F7E[BB_005D5F7E]
  bb_005D5F95[BB_005D5F95]
  bb_005D6010[BB_005D6010]
  bb_005D6025[BB_005D6025]
  bb_005D5F40 -->|branch| bb_005D6010
  bb_005D5F40 -->|fallthrough| bb_005D5F7E
  bb_005D5F7E -->|branch| bb_005D6010
  bb_005D5F7E -->|fallthrough| bb_005D5F95
  bb_005D5F95 -->|flow| bb_005D6010
```
