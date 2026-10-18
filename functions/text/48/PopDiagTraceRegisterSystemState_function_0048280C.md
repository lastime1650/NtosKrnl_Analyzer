# PopDiagTraceRegisterSystemState

- RVA: `0x0048280C`–`0x004828CA` (길이 `190` bytes)
- VA: `0x000000014048280C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000AEDFC`
- 디코드: `37`개 명령, `190/190` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x00482843` → [EtwEventEnabled](../39/EtwEventEnabled_function_00392450.md) (function, `0x00392450`)
- `0x004828B2` → [EtwWriteEx](../25/EtwWriteEx_function_0025F0D0.md) (function, `0x0025F0D0`)
- `0x004828BF` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [PoRegisterSystemState](PoRegisterSystemState_function_00482740.md) at `0x0048276D`

### Static image references
- `0x00482819` → RVA `0x00E0A740` (`.data`; read)
- `0x00482828` → RVA `0x00E67858` (`.data`; read)
- `0x00482835` → RVA `0x00F0B408` (`.data`; read)
- `0x0048283C` → RVA `0x0001A4E0` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0048280C  48 89 54 24 10                  mov qword ptr [rsp + 0x10], rdx
00482811  89 4C 24 08                     mov dword ptr [rsp + 8], ecx
00482815  48 83 EC 78                     sub rsp, 0x78
00482819  48 8B 05 20 7F 98 00            mov rax, qword ptr [rip + 0x987f20]
00482820  48 33 C4                        xor rax, rsp
00482823  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
00482828  80 3D 29 50 9E 00 00            cmp byte ptr [rip + 0x9e5029], 0
0048282F  0F 84 82 00 00 00               je 0x1404828b7
00482835  48 8B 0D CC 8B A8 00            mov rcx, qword ptr [rip + 0xa88bcc]
0048283C  48 8D 15 9D 7C B9 FF            lea rdx, [rip - 0x468363]
00482843  E8 08 FC F0 FF                  call 0x140392450
00482848  84 C0                           test al, al
0048284A  74 6B                           je 0x1404828b7
0048284C  83 64 24 4C 00                  and dword ptr [rsp + 0x4c], 0
00482851  48 8D 84 24 80 00 00 00         lea rax, [rsp + 0x80]
00482859  83 64 24 5C 00                  and dword ptr [rsp + 0x5c], 0
0048285E  48 8D 15 7B 7C B9 FF            lea rdx, [rip - 0x468385]
00482865  48 8B 0D 9C 8B A8 00            mov rcx, qword ptr [rip + 0xa88b9c]
0048286C  45 33 C9                        xor r9d, r9d
0048286F  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00482874  45 33 C0                        xor r8d, r8d
00482877  48 8D 84 24 88 00 00 00         lea rax, [rsp + 0x88]
0048287F  C7 44 24 48 04 00 00 00         mov dword ptr [rsp + 0x48], 4
00482887  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
0048288C  48 8D 44 24 40                  lea rax, [rsp + 0x40]
00482891  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00482896  C7 44 24 30 02 00 00 00         mov dword ptr [rsp + 0x30], 2
0048289E  48 83 64 24 28 00               and qword ptr [rsp + 0x28], 0
004828A4  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
004828AA  C7 44 24 58 08 00 00 00         mov dword ptr [rsp + 0x58], 8
004828B2  E8 19 C8 DD FF                  call 0x14025f0d0
004828B7  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
004828BC  48 33 CC                        xor rcx, rsp
004828BF  E8 7C 9D 22 00                  call 0x1406ac640
004828C4  48 83 C4 78                     add rsp, 0x78
004828C8  C3                              ret
004828C9  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopDiagTraceRegisterSystemState(int a1, __int64 a2, int a3, int a4)
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
    unsigned __int64 v_stack_m40;
    unsigned int v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_p10;
    unsigned int v_stack_p8;

    v_stack_p10 = a2;
    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (120);
    result = (*(unsigned __int64 *)(v_rip + 9994016)) ^ (v_rsp);
    v_stack_m18 = result;
    if ((*(unsigned __int8 *)(v_rip + 10375209)) == 0) goto loc_004828B7;
    result = EtwEventEnabled(*(unsigned __int64 *)(v_rip + 11045836), v_rip - 4621155, a3, a4);
    if ((unsigned __int8)(result) != 0) {
        result = v_stack_p8;
        a2 = v_rip - 4621189;
        a1 = *(unsigned __int64 *)(v_rip + 11045788);
        a4 = 0;
        v_stack_m38 = result;
        a3 = 0;
        result = v_stack_p10;
        v_stack_m30 = 4;
        v_stack_m28 = result;
        result = v_stack_m38;
        v_stack_m40 = result;
        v_stack_m48 = 2;
        v_stack_m20 = 8;
        result = EtwWriteEx(a1, a2, a3, a4);
    }
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (120);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PopDiagTraceRegisterSystemState(int32_t Arg1, int64_t Arg2, int32_t Arg3, int32_t Arg4)
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
    uint64_t v_stack_m40;
    uint32_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_p10;
    uint32_t v_stack_p8;

    v_stack_p10 = Arg2;
    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (120);
    result = (*(uint64_t *)(v_rip + 0x987F20)) ^ (local_rsp);
    v_stack_m18 = result;
    if ((*(uint8_t *)(v_rip + 0x9E5029)) == 0) goto loc_004828B7;
    result = EtwEventEnabled(*(uint64_t *)(v_rip + 0xA88BCC), v_rip - 4621155, Arg3, Arg4);
    if ((uint8_t)(result) != 0) {
        result = v_stack_p8;
        Arg2 = v_rip - 4621189;
        Arg1 = *(uint64_t *)(v_rip + 0xA88B9C);
        Arg4 = 0;
        v_stack_m38 = result;
        Arg3 = 0;
        result = v_stack_p10;
        v_stack_m30 = 4;
        v_stack_m28 = result;
        result = v_stack_m38;
        v_stack_m40 = result;
        v_stack_m48 = 2;
        v_stack_m20 = 8;
        result = EtwWriteEx(Arg1, Arg2, Arg3, Arg4);
    }
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (120);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0048280C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0048280C[BB_0048280C]
  bb_00482835[BB_00482835]
  bb_0048284C[BB_0048284C]
  bb_004828B7[BB_004828B7]
  bb_004828C9[BB_004828C9]
  bb_0048280C -->|branch| bb_004828B7
  bb_0048280C -->|fallthrough| bb_00482835
  bb_00482835 -->|branch| bb_004828B7
  bb_00482835 -->|fallthrough| bb_0048284C
  bb_0048284C -->|flow| bb_004828B7
```
