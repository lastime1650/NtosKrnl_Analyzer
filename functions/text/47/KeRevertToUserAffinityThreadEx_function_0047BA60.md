# KeRevertToUserAffinityThreadEx

- RVA: `0x0047BA60`–`0x0047BAB8` (길이 `88` bytes)
- VA: `0x000000014047BA60`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000AD6FC`
- 디코드: `22`개 명령, `88/88` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0047BA94` → [KeRevertToUserGroupAffinityThread](../39/KeRevertToUserGroupAffinityThread_function_00398EC0.md) (function, `0x00398EC0`)
- `0x0047BAA1` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0047BA64` → RVA `0x00E0A740` (`.data`; read)
- `0x0047BA78` → RVA `0x00FC6AF2` (`ALMOSTRO`; read)
- `0x0047BAAC` → RVA `0x00FC5018` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0047BA60  48 83 EC 48                     sub rsp, 0x48
0047BA64  48 8B 05 D5 EC 98 00            mov rax, qword ptr [rip + 0x98ecd5]
0047BA6B  48 33 C4                        xor rax, rsp
0047BA6E  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0047BA73  0F 57 C0                        xorps xmm0, xmm0
0047BA76  33 C0                           xor eax, eax
0047BA78  38 05 74 B0 B4 00               cmp byte ptr [rip + 0xb4b074], al
0047BA7E  0F 11 44 24 20                  movups xmmword ptr [rsp + 0x20], xmm0
0047BA83  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
0047BA88  75 22                           jne 0x14047baac
0047BA8A  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0047BA8F  66 89 44 24 28                  mov word ptr [rsp + 0x28], ax
0047BA94  E8 27 D4 F1 FF                  call 0x140398ec0
0047BA99  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
0047BA9E  48 33 CC                        xor rcx, rsp
0047BAA1  E8 9A 0B 23 00                  call 0x1406ac640
0047BAA6  48 83 C4 48                     add rsp, 0x48
0047BAAA  C3                              ret
0047BAAB  CC                              int3
0047BAAC  0F B7 05 65 95 B4 00            movzx eax, word ptr [rip + 0xb49565]
0047BAB3  66 FF C8                        dec ax
0047BAB6  EB D2                           jmp 0x14047ba8a
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KeRevertToUserAffinityThreadEx(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int16 v_stack_m20;
    unsigned __int64 v_stack_m28;

    v_rsp = (v_rsp) - (72);
    result = (*(unsigned __int64 *)(v_rip + 10022101)) ^ (v_rsp);
    v_stack_m18 = result;
    result = 0;
    v_stack_m28 = v_xmm0;
    v_stack_m28 = a1;
    if ((*(unsigned __int8 *)(v_rip + 11841652)) != 0) goto loc_0047BAAC;
loc_0047BA8A:
    v_stack_m20 = 0;
    result = KeRevertToUserGroupAffinityThread(v_stack_m28, a2, a3, a4);
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (72);
    return result;
loc_0047BAAC:
    result = (unsigned __int16)((*(unsigned __int16 *)(v_rip + 11834725)) - 1);
    goto loc_0047BA8A;
}
```

## 5. (Beta) C Style

```c
int64_t KeRevertToUserAffinityThreadEx(int64_t Arg1)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint16_t v_stack_m20;
    uint64_t v_stack_m28;

    local_rsp = (local_rsp) - (72);
    result = (*(uint64_t *)(v_rip + 0x98ECD5)) ^ (local_rsp);
    v_stack_m18 = result;
    result = 0;
    v_stack_m28 = v_xmm0;
    v_stack_m28 = Arg1;
    if ((*(uint8_t *)(v_rip + 0xB4B074)) != 0) goto loc_0047BAAC;
loc_0047BA8A:
    v_stack_m20 = 0;
    result = KeRevertToUserGroupAffinityThread(v_stack_m28, a2, a3, a4);
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, a2, a3, a4);
    local_rsp = (local_rsp) + (72);
    return result;
loc_0047BAAC:
    result = (uint16_t)((*(uint16_t *)(v_rip + 0xB49565)) - 1);
    goto loc_0047BA8A;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0047BA60&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0047BA60[BB_0047BA60]
  bb_0047BA8A[BB_0047BA8A]
  bb_0047BAAB[BB_0047BAAB]
  bb_0047BAAC[BB_0047BAAC]
  bb_0047BA60 -->|branch| bb_0047BAAC
  bb_0047BA60 -->|fallthrough| bb_0047BA8A
  bb_0047BAAB -->|flow| bb_0047BAAC
  bb_0047BAAC -->|branch| bb_0047BA8A
```
