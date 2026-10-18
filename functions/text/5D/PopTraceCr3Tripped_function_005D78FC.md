# PopTraceCr3Tripped

- RVA: `0x005D78FC`–`0x005D798F` (길이 `147` bytes)
- VA: `0x00000001405D78FC`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000986E4`
- 디코드: `31`개 명령, `147/147` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x005D792C` → [tlgKeywordOn](../42/tlgKeywordOn_function_0042EAA0.md) (function, `0x0042EAA0`)
- `0x005D7977` → [tlgWriteTransfer_EtwWriteTransfer](../42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (function, `0x004260E0`)
- `0x005D7984` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [sub_006F9E40](../6F/Unknown_function_006F9E40.md) at `0x006F9F15`

### Static image references
- `0x005D7900` → RVA `0x00E0A740` (`.data`; read)
- `0x005D790F` → RVA `0x00E07748` (`.data`; read)
- `0x005D7944` → RVA `0x0004B136` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005D78FC  48 83 EC 78                     sub rsp, 0x78
005D7900  48 8B 05 39 2E 83 00            mov rax, qword ptr [rip + 0x832e39]
005D7907  48 33 C4                        xor rax, rsp
005D790A  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
005D790F  83 3D 32 FE 82 00 05            cmp dword ptr [rip + 0x82fe32], 5
005D7916  44 8B C1                        mov r8d, ecx
005D7919  76 61                           jbe 0x1405d797c
005D791B  48 BA 00 00 00 00 00 40 00 00   movabs rdx, 0x400000000000
005D7925  48 8D 0D 1C FE 82 00            lea rcx, [rip + 0x82fe1c]
005D792C  E8 6F 71 E5 FF                  call 0x14042eaa0
005D7931  84 C0                           test al, al
005D7933  74 47                           je 0x1405d797c
005D7935  83 64 24 64 00                  and dword ptr [rsp + 0x64], 0
005D793A  48 8D 44 24 30                  lea rax, [rsp + 0x30]
005D793F  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
005D7944  48 8D 15 EB 37 A7 FF            lea rdx, [rip - 0x58c815]
005D794B  48 8D 44 24 38                  lea rax, [rsp + 0x38]
005D7950  44 89 44 24 30                  mov dword ptr [rsp + 0x30], r8d
005D7955  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
005D795A  48 8D 0D E7 FD 82 00            lea rcx, [rip + 0x82fde7]
005D7961  45 33 C9                        xor r9d, r9d
005D7964  C7 44 24 20 03 00 00 00         mov dword ptr [rsp + 0x20], 3
005D796C  45 33 C0                        xor r8d, r8d
005D796F  C7 44 24 60 04 00 00 00         mov dword ptr [rsp + 0x60], 4
005D7977  E8 64 E7 E4 FF                  call 0x1404260e0
005D797C  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
005D7981  48 33 CC                        xor rcx, rsp
005D7984  E8 B7 4C 0D 00                  call 0x1406ac640
005D7989  48 83 C4 78                     add rsp, 0x78
005D798D  C3                              ret
005D798E  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopTraceCr3Tripped(int a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m10;
    unsigned int v_stack_m14;
    unsigned int v_stack_m18;
    unsigned __int64 v_stack_m20;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned int v_stack_m58;

    v_rsp = (v_rsp) - (120);
    result = (*(unsigned __int64 *)(v_rip + 8597049)) ^ (v_rsp);
    v_stack_m10 = result;
    if ((*(unsigned int *)(v_rip + 8584754)) <= 5) goto loc_005D797C;
    result = tlgKeywordOn(v_rip + 8584732, a2, (unsigned int)(a1), a4);
    if ((unsigned __int8)(result) != 0) {
        result = v_stack_m48;
        v_stack_m20 = result;
        a2 = v_rip - 5818389;
        result = v_stack_m40;
        v_stack_m48 = (unsigned int)((unsigned int)(a1));
        v_stack_m50 = result;
        a1 = v_rip + 8584679;
        a4 = 0;
        v_stack_m58 = 3;
        a3 = 0;
        v_stack_m18 = 4;
        result = tlgWriteTransfer_EtwWriteTransfer(a1, a2, a3, a4);
    }
    a1 = (v_stack_m10) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (120);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PopTraceCr3Tripped(int32_t Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m10;
    uint32_t v_stack_m14;
    uint32_t v_stack_m18;
    uint64_t v_stack_m20;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint32_t v_stack_m58;

    local_rsp = (local_rsp) - (120);
    result = (*(uint64_t *)(v_rip + 0x832E39)) ^ (local_rsp);
    v_stack_m10 = result;
    if ((*(uint32_t *)(v_rip + 0x82FE32)) <= 5) goto loc_005D797C;
    result = tlgKeywordOn(v_rip + 8584732, Arg2, (uint32_t)(Arg1), Arg4);
    if ((uint8_t)(result) != 0) {
        result = v_stack_m48;
        v_stack_m20 = result;
        Arg2 = v_rip - 5818389;
        result = v_stack_m40;
        v_stack_m48 = (uint32_t)((uint32_t)(Arg1));
        v_stack_m50 = result;
        Arg1 = v_rip + 8584679;
        Arg4 = 0;
        v_stack_m58 = 3;
        Arg3 = 0;
        v_stack_m18 = 4;
        result = tlgWriteTransfer_EtwWriteTransfer(Arg1, Arg2, Arg3, Arg4);
    }
    Arg1 = (v_stack_m10) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (120);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005D78FC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005D78FC[BB_005D78FC]
  bb_005D791B[BB_005D791B]
  bb_005D7935[BB_005D7935]
  bb_005D797C[BB_005D797C]
  bb_005D798E[BB_005D798E]
  bb_005D78FC -->|branch| bb_005D797C
  bb_005D78FC -->|fallthrough| bb_005D791B
  bb_005D791B -->|branch| bb_005D797C
  bb_005D791B -->|fallthrough| bb_005D7935
  bb_005D7935 -->|flow| bb_005D797C
```
