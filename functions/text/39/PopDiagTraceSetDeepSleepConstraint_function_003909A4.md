# PopDiagTraceSetDeepSleepConstraint

- RVA: `0x003909A4`–`0x00390A3C` (길이 `152` bytes)
- VA: `0x00000001403909A4`
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
- `0x003909D2` → [EtwEventEnabled](EtwEventEnabled_function_00392450.md) (function, `0x00392450`)
- `0x00390A24` → [EtwWriteEx](../25/EtwWriteEx_function_0025F0D0.md) (function, `0x0025F0D0`)
- `0x00390A31` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [PopDeepSleepSetDisengageReason](../38/PopDeepSleepSetDisengageReason_function_0038FEC4.md) at `0x0038FF34`

### Static image references
- `0x003909AC` → RVA `0x00E0A740` (`.data`; read)
- `0x003909BB` → RVA `0x00E67858` (`.data`; read)
- `0x003909C4` → RVA `0x00F0B408` (`.data`; read)
- `0x003909CB` → RVA `0x000112F0` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
003909A4  89 4C 24 08                     mov dword ptr [rsp + 8], ecx
003909A8  48 83 EC 68                     sub rsp, 0x68
003909AC  48 8B 05 8D 9D A7 00            mov rax, qword ptr [rip + 0xa79d8d]
003909B3  48 33 C4                        xor rax, rsp
003909B6  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
003909BB  80 3D 96 6E AD 00 00            cmp byte ptr [rip + 0xad6e96], 0
003909C2  74 65                           je 0x140390a29
003909C4  48 8B 0D 3D AA B7 00            mov rcx, qword ptr [rip + 0xb7aa3d]
003909CB  48 8D 15 1E 09 C8 FF            lea rdx, [rip - 0x37f6e2]
003909D2  E8 79 1A 00 00                  call 0x140392450
003909D7  84 C0                           test al, al
003909D9  74 4E                           je 0x140390a29
003909DB  83 64 24 4C 00                  and dword ptr [rsp + 0x4c], 0
003909E0  48 8D 44 24 70                  lea rax, [rsp + 0x70]
003909E5  48 8B 0D 1C AA B7 00            mov rcx, qword ptr [rip + 0xb7aa1c]
003909EC  48 8D 15 FD 08 C8 FF            lea rdx, [rip - 0x37f703]
003909F3  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
003909F8  45 33 C9                        xor r9d, r9d
003909FB  48 8D 44 24 40                  lea rax, [rsp + 0x40]
00390A00  C7 44 24 48 04 00 00 00         mov dword ptr [rsp + 0x48], 4
00390A08  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00390A0D  45 33 C0                        xor r8d, r8d
00390A10  C7 44 24 30 01 00 00 00         mov dword ptr [rsp + 0x30], 1
00390A18  48 83 64 24 28 00               and qword ptr [rsp + 0x28], 0
00390A1E  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
00390A24  E8 A7 E6 EC FF                  call 0x14025f0d0
00390A29  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
00390A2E  48 33 CC                        xor rcx, rsp
00390A31  E8 0A BC 31 00                  call 0x1406ac640
00390A36  48 83 C4 68                     add rsp, 0x68
00390A3A  C3                              ret
00390A3B  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopDiagTraceSetDeepSleepConstraint(int a1, __int64 a2, int a3, int a4)
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
    result = (*(unsigned __int64 *)(v_rip + 10984845)) ^ (v_rsp);
    v_stack_m18 = result;
    if ((*(unsigned __int8 *)(v_rip + 11366038)) == 0) goto loc_00390A29;
    result = EtwEventEnabled(*(unsigned __int64 *)(v_rip + 12036669), v_rip - 3667682, a3, a4);
    if ((unsigned __int8)(result) != 0) {
        result = v_stack_p8;
        a1 = *(unsigned __int64 *)(v_rip + 12036636);
        a2 = v_rip - 3667715;
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
int64_t PopDiagTraceSetDeepSleepConstraint(int32_t Arg1, int64_t Arg2, int32_t Arg3, int32_t Arg4)
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
    result = (*(uint64_t *)(v_rip + 0xA79D8D)) ^ (local_rsp);
    v_stack_m18 = result;
    if ((*(uint8_t *)(v_rip + 0xAD6E96)) == 0) goto loc_00390A29;
    result = EtwEventEnabled(*(uint64_t *)(v_rip + 0xB7AA3D), v_rip - 3667682, Arg3, Arg4);
    if ((uint8_t)(result) != 0) {
        result = v_stack_p8;
        Arg1 = *(uint64_t *)(v_rip + 0xB7AA1C);
        Arg2 = v_rip - 3667715;
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

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003909A4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_003909A4[BB_003909A4]
  bb_003909C4[BB_003909C4]
  bb_003909DB[BB_003909DB]
  bb_00390A29[BB_00390A29]
  bb_00390A3B[BB_00390A3B]
  bb_003909A4 -->|branch| bb_00390A29
  bb_003909A4 -->|fallthrough| bb_003909C4
  bb_003909C4 -->|branch| bb_00390A29
  bb_003909C4 -->|fallthrough| bb_003909DB
  bb_003909DB -->|flow| bb_00390A29
```
