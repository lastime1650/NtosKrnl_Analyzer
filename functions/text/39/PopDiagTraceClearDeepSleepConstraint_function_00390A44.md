# PopDiagTraceClearDeepSleepConstraint

- RVA: `0x00390A44`–`0x00390ADC` (길이 `152` bytes)
- VA: `0x0000000140390A44`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00073440`
- 디코드: `32`개 명령, `152/152` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x00390A72` → [EtwEventEnabled](EtwEventEnabled_function_00392450.md) (function, `0x00392450`)
- `0x00390AC4` → [EtwWriteEx](../25/EtwWriteEx_function_0025F0D0.md) (function, `0x0025F0D0`)
- `0x00390AD1` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [PopDeepSleepClearDisengageReason](PopDeepSleepClearDisengageReason_function_0039010C.md) at `0x00390147`

### Static image references
- `0x00390A4C` → RVA `0x00E0A740` (`.data`; read)
- `0x00390A5B` → RVA `0x00E67858` (`.data`; read)
- `0x00390A64` → RVA `0x00F0B408` (`.data`; read)
- `0x00390A6B` → RVA `0x000112E0` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00390A44  89 4C 24 08                     mov dword ptr [rsp + 8], ecx
00390A48  48 83 EC 68                     sub rsp, 0x68
00390A4C  48 8B 05 ED 9C A7 00            mov rax, qword ptr [rip + 0xa79ced]
00390A53  48 33 C4                        xor rax, rsp
00390A56  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
00390A5B  80 3D F6 6D AD 00 00            cmp byte ptr [rip + 0xad6df6], 0
00390A62  74 65                           je 0x140390ac9
00390A64  48 8B 0D 9D A9 B7 00            mov rcx, qword ptr [rip + 0xb7a99d]
00390A6B  48 8D 15 6E 08 C8 FF            lea rdx, [rip - 0x37f792]
00390A72  E8 D9 19 00 00                  call 0x140392450
00390A77  84 C0                           test al, al
00390A79  74 4E                           je 0x140390ac9
00390A7B  83 64 24 4C 00                  and dword ptr [rsp + 0x4c], 0
00390A80  48 8D 44 24 70                  lea rax, [rsp + 0x70]
00390A85  48 8B 0D 7C A9 B7 00            mov rcx, qword ptr [rip + 0xb7a97c]
00390A8C  48 8D 15 4D 08 C8 FF            lea rdx, [rip - 0x37f7b3]
00390A93  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00390A98  45 33 C9                        xor r9d, r9d
00390A9B  48 8D 44 24 40                  lea rax, [rsp + 0x40]
00390AA0  C7 44 24 48 04 00 00 00         mov dword ptr [rsp + 0x48], 4
00390AA8  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00390AAD  45 33 C0                        xor r8d, r8d
00390AB0  C7 44 24 30 01 00 00 00         mov dword ptr [rsp + 0x30], 1
00390AB8  48 83 64 24 28 00               and qword ptr [rsp + 0x28], 0
00390ABE  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
00390AC4  E8 07 E6 EC FF                  call 0x14025f0d0
00390AC9  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
00390ACE  48 33 CC                        xor rcx, rsp
00390AD1  E8 6A BB 31 00                  call 0x1406ac640
00390AD6  48 83 C4 68                     add rsp, 0x68
00390ADA  C3                              ret
00390ADB  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopDiagTraceClearDeepSleepConstraint(int a1, __int64 a2, int a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned int v_stack_m1C;
    unsigned int v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned int v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned int v_stack_p8;

    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (104);
    result = (*(unsigned __int64 *)(v_rip + 10984685)) ^ (v_rsp);
    v_stack_m18 = result;
    if ((*(unsigned __int8 *)(v_rip + 11365878)) == 0) goto loc_00390AC9;
    result = EtwEventEnabled(*(unsigned __int64 *)(v_rip + 12036509), v_rip - 3667858, a3, a4);
    if ((unsigned __int8)(result) != 0) {
        result = v_stack_p8;
        a1 = *(unsigned __int64 *)(v_rip + 12036476);
        a2 = v_rip - 3667891;
        v_stack_m28 = result;
        a4 = 0;
        result = v_stack_m28;
        v_stack_m20 = 4;
        v_stack_m30 = result;
        a3 = 0;
        v_stack_m38 = 1;
        result = EtwWriteEx(a1, a2, a3, a4);
    }
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (104);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PopDiagTraceClearDeepSleepConstraint(int32_t Arg1, int64_t Arg2, int32_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint32_t v_stack_m1C;
    uint32_t v_stack_m20;
    uint64_t v_stack_m28;
    uint64_t v_stack_m30;
    uint32_t v_stack_m38;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint32_t v_stack_p8;

    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (104);
    result = (*(uint64_t *)(v_rip + 0xA79CED)) ^ (local_rsp);
    v_stack_m18 = result;
    if ((*(uint8_t *)(v_rip + 0xAD6DF6)) == 0) goto loc_00390AC9;
    result = EtwEventEnabled(*(uint64_t *)(v_rip + 0xB7A99D), v_rip - 3667858, Arg3, Arg4);
    if ((uint8_t)(result) != 0) {
        result = v_stack_p8;
        Arg1 = *(uint64_t *)(v_rip + 0xB7A97C);
        Arg2 = v_rip - 3667891;
        v_stack_m28 = result;
        Arg4 = 0;
        result = v_stack_m28;
        v_stack_m20 = 4;
        v_stack_m30 = result;
        Arg3 = 0;
        v_stack_m38 = 1;
        result = EtwWriteEx(Arg1, Arg2, Arg3, Arg4);
    }
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (104);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00390A44&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00390A44[BB_00390A44]
  bb_00390A64[BB_00390A64]
  bb_00390A7B[BB_00390A7B]
  bb_00390AC9[BB_00390AC9]
  bb_00390ADB[BB_00390ADB]
  bb_00390A44 -->|branch| bb_00390AC9
  bb_00390A44 -->|fallthrough| bb_00390A64
  bb_00390A64 -->|branch| bb_00390AC9
  bb_00390A64 -->|fallthrough| bb_00390A7B
  bb_00390A7B -->|flow| bb_00390AC9
```
