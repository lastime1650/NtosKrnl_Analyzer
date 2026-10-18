# IopDumpTraceInitializeDumpStackFailure

- RVA: `0x005951A8`–`0x005952B0` (길이 `264` bytes)
- VA: `0x00000001405951A8`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BF3A4`
- 디코드: `57`개 명령, `264/264` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **5**; 고유 호출 대상: **5**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **5**

### Outgoing calls
- `0x005951C7` → [IopDumpIsTracingEnabled](../4F/IopDumpIsTracingEnabled_function_004FC5D0.md) (function, `0x004FC5D0`)
- `0x00595214` → [EtwWriteEx](../25/EtwWriteEx_function_0025F0D0.md) (function, `0x0025F0D0`)
- `0x00595233` → [tlgKeywordOn](../42/tlgKeywordOn_function_0042EAA0.md) (function, `0x0042EAA0`)
- `0x00595295` → [tlgWriteTransfer_EtwWriteTransfer](../42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (function, `0x004260E0`)
- `0x005952A1` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [IoInitializeDumpStack](IoInitializeDumpStack_function_00592A50.md) at `0x00592A89`

### Static image references
- `0x005951B9` → RVA `0x00E0A740` (`.data`; read)
- `0x005951D8` → RVA `0x00E65EF0` (`.data`; read)
- `0x005951DF` → RVA `0x00023208` (`.rdata`; read)
- `0x00595219` → RVA `0x00E06DE8` (`.data`; read)
- `0x00595248` → RVA `0x00045C69` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005951A8  89 4C 24 08                     mov dword ptr [rsp + 8], ecx
005951AC  55                              push rbp
005951AD  48 8D 6C 24 A9                  lea rbp, [rsp - 0x57]
005951B2  48 81 EC B0 00 00 00            sub rsp, 0xb0
005951B9  48 8B 05 80 55 87 00            mov rax, qword ptr [rip + 0x875580]
005951C0  48 33 C4                        xor rax, rsp
005951C3  48 89 45 47                     mov qword ptr [rbp + 0x47], rax
005951C7  E8 04 74 F6 FF                  call 0x1404fc5d0
005951CC  84 C0                           test al, al
005951CE  74 49                           je 0x140595219
005951D0  83 65 03 00                     and dword ptr [rbp + 3], 0
005951D4  48 8D 45 67                     lea rax, [rbp + 0x67]
005951D8  48 8B 0D 11 0D 8D 00            mov rcx, qword ptr [rip + 0x8d0d11]
005951DF  48 8D 15 22 E0 A8 FF            lea rdx, [rip - 0x571fde]
005951E6  48 89 45 F7                     mov qword ptr [rbp - 9], rax
005951EA  45 33 C9                        xor r9d, r9d
005951ED  48 8D 45 F7                     lea rax, [rbp - 9]
005951F1  C7 45 FF 04 00 00 00            mov dword ptr [rbp - 1], 4
005951F8  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
005951FD  45 33 C0                        xor r8d, r8d
00595200  C7 44 24 30 01 00 00 00         mov dword ptr [rsp + 0x30], 1
00595208  48 83 64 24 28 00               and qword ptr [rsp + 0x28], 0
0059520E  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
00595214  E8 B7 9E CC FF                  call 0x14025f0d0
00595219  83 3D C8 1B 87 00 05            cmp dword ptr [rip + 0x871bc8], 5
00595220  76 78                           jbe 0x14059529a
00595222  48 BA 00 00 00 00 00 40 00 00   movabs rdx, 0x400000000000
0059522C  48 8D 0D B5 1B 87 00            lea rcx, [rip + 0x871bb5]
00595233  E8 68 98 E9 FF                  call 0x14042eaa0
00595238  84 C0                           test al, al
0059523A  74 5E                           je 0x14059529a
0059523C  83 65 33 00                     and dword ptr [rbp + 0x33], 0
00595240  48 8D 45 EF                     lea rax, [rbp - 0x11]
00595244  83 65 43 00                     and dword ptr [rbp + 0x43], 0
00595248  48 8D 15 1A 0A AB FF            lea rdx, [rip - 0x54f5e6]
0059524F  48 89 45 27                     mov qword ptr [rbp + 0x27], rax
00595253  48 8D 0D 8E 1B 87 00            lea rcx, [rip + 0x871b8e]
0059525A  8B 45 67                        mov eax, dword ptr [rbp + 0x67]
0059525D  45 33 C9                        xor r9d, r9d
00595260  89 45 E7                        mov dword ptr [rbp - 0x19], eax
00595263  45 33 C0                        xor r8d, r8d
00595266  48 8D 45 E7                     lea rax, [rbp - 0x19]
0059526A  48 C7 45 EF 00 00 00 01         mov qword ptr [rbp - 0x11], 0x1000000
00595272  48 89 45 37                     mov qword ptr [rbp + 0x37], rax
00595276  48 8D 45 07                     lea rax, [rbp + 7]
0059527A  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0059527F  C7 44 24 20 04 00 00 00         mov dword ptr [rsp + 0x20], 4
00595287  C7 45 2F 08 00 00 00            mov dword ptr [rbp + 0x2f], 8
0059528E  C7 45 3F 04 00 00 00            mov dword ptr [rbp + 0x3f], 4
00595295  E8 46 0E E9 FF                  call 0x1404260e0
0059529A  48 8B 4D 47                     mov rcx, qword ptr [rbp + 0x47]
0059529E  48 33 CC                        xor rcx, rsp
005952A1  E8 9A 73 11 00                  call 0x1406ac640
005952A6  48 81 C4 B0 00 00 00            add rsp, 0xb0
005952AD  5D                              pop rbp
005952AE  C3                              ret
005952AF  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IopDumpTraceInitializeDumpStackFailure(int a1, __int64 a2, int a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned int v_stack_m1C;
    unsigned int v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned int v_stack_m2C;
    unsigned int v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m58;
    unsigned int v_stack_m5C;
    unsigned __int64 v_stack_m5F;
    unsigned int v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned int v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned int v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned int v_stack_p8;

    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (176);
    result = (*(unsigned __int64 *)(v_rip + 8869248)) ^ (v_rsp);
    v_stack_m18 = result;
    result = IopDumpIsTracingEnabled(a1, a2, a3, a4);
    if ((unsigned __int8)(result) != 0) {
        result = v_stack_p8;
        a1 = *(unsigned __int64 *)(v_rip + 9243921);
        a2 = v_rip - 5709790;
        v_stack_m68 = result;
        a4 = 0;
        result = v_stack_m68;
        v_stack_m60 = 4;
        v_stack_m80 = result;
        a3 = 0;
        v_stack_m88 = 1;
        result = EtwWriteEx(a1, a2, a3, a4);
    }
    if ((*(unsigned int *)(v_rip + 8854472)) <= 5) goto loc_0059529A;
    result = tlgKeywordOn(v_rip + 8854453, a2, a3, a4);
    if ((unsigned __int8)(result) != 0) {
        result = v_stack_m70;
        a2 = v_rip - 5567974;
        v_stack_m38 = result;
        a1 = v_rip + 8854414;
        result = v_stack_p8;
        a4 = 0;
        v_stack_m78 = (unsigned int)(result);
        a3 = 0;
        result = v_stack_m78;
        v_stack_m70 = 0x1000000ULL;
        v_stack_m28 = result;
        result = v_stack_m58;
        v_stack_m90 = result;
        v_stack_m98 = 4;
        v_stack_m30 = 8;
        v_stack_m20 = 4;
        result = tlgWriteTransfer_EtwWriteTransfer(a1, a2, a3, a4);
    }
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (176);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t IopDumpTraceInitializeDumpStackFailure(int32_t Arg1, int64_t Arg2, int32_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint32_t v_stack_m1C;
    uint32_t v_stack_m20;
    uint64_t v_stack_m28;
    uint32_t v_stack_m2C;
    uint32_t v_stack_m30;
    uint64_t v_stack_m38;
    uint64_t v_stack_m58;
    uint32_t v_stack_m5C;
    uint64_t v_stack_m5F;
    uint32_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint32_t v_stack_m78;
    uint64_t v_stack_m80;
    uint32_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint32_t v_stack_p8;

    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (176);
    result = (*(uint64_t *)(v_rip + 0x875580)) ^ (local_rsp);
    v_stack_m18 = result;
    result = IopDumpIsTracingEnabled(Arg1, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) != 0) {
        result = v_stack_p8;
        Arg1 = *(uint64_t *)(v_rip + 0x8D0D11);
        Arg2 = v_rip - 5709790;
        v_stack_m68 = result;
        Arg4 = 0;
        result = v_stack_m68;
        v_stack_m60 = 4;
        v_stack_m80 = result;
        Arg3 = 0;
        v_stack_m88 = 1;
        result = EtwWriteEx(Arg1, Arg2, Arg3, Arg4);
    }
    if ((*(uint32_t *)(v_rip + 0x871BC8)) <= 5) goto loc_0059529A;
    result = tlgKeywordOn(v_rip + 8854453, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) != 0) {
        result = v_stack_m70;
        Arg2 = v_rip - 5567974;
        v_stack_m38 = result;
        Arg1 = v_rip + 8854414;
        result = v_stack_p8;
        Arg4 = 0;
        v_stack_m78 = (uint32_t)(result);
        Arg3 = 0;
        result = v_stack_m78;
        v_stack_m70 = 0x1000000ULL;
        v_stack_m28 = result;
        result = v_stack_m58;
        v_stack_m90 = result;
        v_stack_m98 = 4;
        v_stack_m30 = 8;
        v_stack_m20 = 4;
        result = tlgWriteTransfer_EtwWriteTransfer(Arg1, Arg2, Arg3, Arg4);
    }
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (176);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005951A8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005951A8[BB_005951A8]
  bb_005951D0[BB_005951D0]
  bb_00595219[BB_00595219]
  bb_00595222[BB_00595222]
  bb_0059523C[BB_0059523C]
  bb_0059529A[BB_0059529A]
  bb_005952AF[BB_005952AF]
  bb_005951A8 -->|branch| bb_00595219
  bb_005951A8 -->|fallthrough| bb_005951D0
  bb_005951D0 -->|flow| bb_00595219
  bb_00595219 -->|branch| bb_0059529A
  bb_00595219 -->|fallthrough| bb_00595222
  bb_00595222 -->|branch| bb_0059529A
  bb_00595222 -->|fallthrough| bb_0059523C
  bb_0059523C -->|flow| bb_0059529A
```
