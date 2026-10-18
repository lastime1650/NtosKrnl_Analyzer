# PpmEventTraceProfileEnable

- RVA: `0x00ABD348`–`0x00ABD3DA` (길이 `146` bytes)
- VA: `0x0000000140ABD348`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BD524`
- 디코드: `35`개 명령, `146/146` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **5**

### Outgoing calls
- `0x00ABD387` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (function, `0x00392450`)
- `0x00ABD3C1` → [EtwWrite](../../text/41/EtwWrite_function_0041C720.md) (function, `0x0041C720`)
- `0x00ABD3CE` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [PpmDisableProfile](../77/PpmDisableProfile_function_00770858.md) at `0x007708FF`
- [PpmEnableProfile](../77/PpmEnableProfile_function_00770938.md) at `0x007709CC`

### Static image references
- `0x00ABD351` → RVA `0x00E0A740` (`.data`; read)
- `0x00ABD362` → RVA `0x0001E330` (`.rdata`; read)
- `0x00ABD369` → RVA `0x0001E340` (`.rdata`; read)
- `0x00ABD374` → RVA `0x00E67A39` (`.data`; read)
- `0x00ABD37D` → RVA `0x00F083E8` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x00ABD387` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (`PAGE` → `.text`)
  - `0x00ABD3C1` → [EtwWrite](../../text/41/EtwWrite_function_0041C720.md) (`PAGE` → `.text`)
  - `0x00ABD3CE` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00ABD348  88 4C 24 08                     mov byte ptr [rsp + 8], cl
00ABD34C  53                              push rbx
00ABD34D  48 83 EC 50                     sub rsp, 0x50
00ABD351  48 8B 05 E8 D3 34 00            mov rax, qword ptr [rip + 0x34d3e8]
00ABD358  48 33 C4                        xor rax, rsp
00ABD35B  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00ABD360  84 D2                           test dl, dl
00ABD362  48 8D 05 C7 0F 56 FF            lea rax, [rip - 0xa9f039]
00ABD369  48 8D 1D D0 0F 56 FF            lea rbx, [rip - 0xa9f030]
00ABD370  48 0F 44 D8                     cmove rbx, rax
00ABD374  80 3D BE A6 3A 00 00            cmp byte ptr [rip + 0x3aa6be], 0
00ABD37B  74 49                           je 0x140abd3c6
00ABD37D  48 8B 0D 64 B0 44 00            mov rcx, qword ptr [rip + 0x44b064]
00ABD384  48 8B D3                        mov rdx, rbx
00ABD387  E8 C4 50 8D FF                  call 0x140392450
00ABD38C  84 C0                           test al, al
00ABD38E  74 36                           je 0x140abd3c6
00ABD390  83 64 24 3C 00                  and dword ptr [rsp + 0x3c], 0
00ABD395  48 8D 44 24 60                  lea rax, [rsp + 0x60]
00ABD39A  48 8B 0D 47 B0 44 00            mov rcx, qword ptr [rip + 0x44b047]
00ABD3A1  41 B9 01 00 00 00               mov r9d, 1
00ABD3A7  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00ABD3AC  45 33 C0                        xor r8d, r8d
00ABD3AF  48 8D 44 24 30                  lea rax, [rsp + 0x30]
00ABD3B4  44 89 4C 24 38                  mov dword ptr [rsp + 0x38], r9d
00ABD3B9  48 8B D3                        mov rdx, rbx
00ABD3BC  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00ABD3C1  E8 5A F3 95 FF                  call 0x14041c720
00ABD3C6  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00ABD3CB  48 33 CC                        xor rcx, rsp
00ABD3CE  E8 6D F2 BE FF                  call 0x1406ac640
00ABD3D3  48 83 C4 50                     add rsp, 0x50
00ABD3D7  5B                              pop rbx
00ABD3D8  C3                              ret
00ABD3D9  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PpmEventTraceProfileEnable(unsigned __int8 a1, unsigned __int8 a2, int a3)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned int v_stack_m1C;
    unsigned int v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m38;
    unsigned __int8 v_stack_p8;

    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (80);
    result = (*(unsigned __int64 *)(v_rip + 3462120)) ^ (v_rsp);
    v_stack_m18 = result;
    v_rbx = v_rip - 11137072;
    if (a2 == 0) { v_rbx = v_rip - 11137081; }
    if ((*(unsigned __int8 *)(v_rip + 3843774)) == 0) goto loc_00ABD3C6;
    result = EtwEventEnabled(*(unsigned __int64 *)(v_rip + 4501604), v_rbx, a3, a4);
    if ((unsigned __int8)(result) != 0) {
        result = v_stack_p8;
        a1 = *(unsigned __int64 *)(v_rip + 4501575);
        a4 = 1;
        v_stack_m28 = result;
        a3 = 0;
        result = v_stack_m28;
        v_stack_m20 = (unsigned int)(a4);
        a2 = v_rbx;
        v_stack_m38 = result;
        result = EtwWrite(a1, a2, a3, a4);
    }
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (80);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PpmEventTraceProfileEnable(uint8_t Arg1, uint8_t Arg2, int32_t Arg3)
{
    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint32_t v_stack_m1C;
    uint32_t v_stack_m20;
    uint64_t v_stack_m28;
    uint64_t v_stack_m38;
    uint8_t v_stack_p8;

    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (80);
    result = (*(uint64_t *)(v_rip + 0x34D3E8)) ^ (local_rsp);
    v_stack_m18 = result;
    local_rbx = v_rip - 11137072;
    if (Arg2 == 0) { local_rbx = v_rip - 11137081; }
    if ((*(uint8_t *)(v_rip + 0x3AA6BE)) == 0) goto loc_00ABD3C6;
    result = EtwEventEnabled(*(uint64_t *)(v_rip + 0x44B064), local_rbx, Arg3, a4);
    if ((uint8_t)(result) != 0) {
        result = v_stack_p8;
        Arg1 = *(uint64_t *)(v_rip + 0x44B047);
        a4 = 1;
        v_stack_m28 = result;
        Arg3 = 0;
        result = v_stack_m28;
        v_stack_m20 = (uint32_t)(a4);
        Arg2 = local_rbx;
        v_stack_m38 = result;
        result = EtwWrite(Arg1, Arg2, Arg3, a4);
    }
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, a4);
    local_rsp = (local_rsp) + (80);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00ABD348&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00ABD348[BB_00ABD348]
  bb_00ABD37D[BB_00ABD37D]
  bb_00ABD390[BB_00ABD390]
  bb_00ABD3C6[BB_00ABD3C6]
  bb_00ABD3D9[BB_00ABD3D9]
  bb_00ABD348 -->|branch| bb_00ABD3C6
  bb_00ABD348 -->|fallthrough| bb_00ABD37D
  bb_00ABD37D -->|branch| bb_00ABD3C6
  bb_00ABD37D -->|fallthrough| bb_00ABD390
  bb_00ABD390 -->|flow| bb_00ABD3C6
```
