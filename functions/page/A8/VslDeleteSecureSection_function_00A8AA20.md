# VslDeleteSecureSection

- RVA: `0x00A8AA20`–`0x00A8AA81` (길이 `97` bytes)
- VA: `0x0000000140A8AA20`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000AF554`
- 디코드: `23`개 명령, `97/97` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00A8AA49` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00A8AA62` → [VslpEnterIumSecureMode](../../text/23/VslpEnterIumSecureMode_function_00235E50.md) (function, `0x00235E50`)
- `0x00A8AA72` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00A8AA29` → RVA `0x00E0A740` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x00A8AA49` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00A8AA62` → [VslpEnterIumSecureMode](../../text/23/VslpEnterIumSecureMode_function_00235E50.md) (`PAGE` → `.text`)
  - `0x00A8AA72` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A8AA20  40 53                           push rbx
00A8AA22  48 81 EC A0 00 00 00            sub rsp, 0xa0
00A8AA29  48 8B 05 10 FD 37 00            mov rax, qword ptr [rip + 0x37fd10]
00A8AA30  48 33 C4                        xor rax, rsp
00A8AA33  48 89 84 24 90 00 00 00         mov qword ptr [rsp + 0x90], rax
00A8AA3B  33 D2                           xor edx, edx
00A8AA3D  48 8B D9                        mov rbx, rcx
00A8AA40  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00A8AA45  44 8D 42 68                     lea r8d, [rdx + 0x68]
00A8AA49  E8 F2 C1 C3 FF                  call 0x1406c6c40
00A8AA4E  BA 45 00 00 00                  mov edx, 0x45
00A8AA53  48 89 5C 24 28                  mov qword ptr [rsp + 0x28], rbx
00A8AA58  4C 8D 4C 24 20                  lea r9, [rsp + 0x20]
00A8AA5D  45 33 C0                        xor r8d, r8d
00A8AA60  B1 02                           mov cl, 2
00A8AA62  E8 E9 B3 7A FF                  call 0x140235e50
00A8AA67  48 8B 8C 24 90 00 00 00         mov rcx, qword ptr [rsp + 0x90]
00A8AA6F  48 33 CC                        xor rcx, rsp
00A8AA72  E8 C9 1B C2 FF                  call 0x1406ac640
00A8AA77  48 81 C4 A0 00 00 00            add rsp, 0xa0
00A8AA7E  5B                              pop rbx
00A8AA7F  C3                              ret
00A8AA80  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall VslDeleteSecureSection(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;

    v_rsp = (v_rsp) - (160);
    result = (*(unsigned __int64 *)(v_rip + 3669264)) ^ (v_rsp);
    v_stack_m18 = result;
    a2 = 0;
    result = memset(v_stack_m88, a2, a2 + 104, a4);
    v_stack_m80 = a1;
    a3 = 0;
    result = VslpEnterIumSecureMode(2, 69, a3, v_stack_m88);
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, 69, a3, v_stack_m88);
    v_rsp = (v_rsp) + (160);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t VslDeleteSecureSection(int64_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;

    local_rsp = (local_rsp) - (160);
    result = (*(uint64_t *)(v_rip + 0x37FD10)) ^ (local_rsp);
    v_stack_m18 = result;
    Arg2 = 0;
    result = memset(v_stack_m88, Arg2, Arg2 + 104, a4);
    v_stack_m80 = Arg1;
    a3 = 0;
    result = VslpEnterIumSecureMode(2, 69, a3, v_stack_m88);
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, 69, a3, v_stack_m88);
    local_rsp = (local_rsp) + (160);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A8AA20&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A8AA20[BB_00A8AA20]
  bb_00A8AA80[BB_00A8AA80]
```
