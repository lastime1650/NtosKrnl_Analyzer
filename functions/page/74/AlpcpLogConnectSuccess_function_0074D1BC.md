# AlpcpLogConnectSuccess

- RVA: `0x0074D1BC`–`0x0074D220` (길이 `100` bytes)
- VA: `0x000000014074D1BC`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00060904`
- 디코드: `21`개 명령, `100/100` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0074D208` → [AlpcpInvokeLogCallbacks](../AC/AlpcpInvokeLogCallbacks_function_00AC40D0.md) (function, `0x00AC40D0`)
- `0x0074D215` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [NtSecureConnectPort](../92/NtSecureConnectPort_function_00922F20.md) at `0x0092351A`
- [AlpcpProcessConnectionRequest](../92/AlpcpProcessConnectionRequest_function_00925FD4.md) at `0x009264C9`

### Static image references
- `0x0074D1C0` → RVA `0x00E0A740` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0074D215` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0074D1BC  48 83 EC 58                     sub rsp, 0x58
0074D1C0  48 8B 05 79 D5 6B 00            mov rax, qword ptr [rip + 0x6bd579]
0074D1C7  48 33 C4                        xor rax, rsp
0074D1CA  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
0074D1CF  0F 57 C0                        xorps xmm0, xmm0
0074D1D2  BA 1C 00 00 00                  mov edx, 0x1c
0074D1D7  0F 11 44 24 30                  movups xmmword ptr [rsp + 0x30], xmm0
0074D1DC  0F 11 44 24 20                  movups xmmword ptr [rsp + 0x20], xmm0
0074D1E1  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0074D1EA  0F 10 80 08 05 00 00            movups xmm0, xmmword ptr [rax + 0x508]
0074D1F1  89 4C 24 38                     mov dword ptr [rsp + 0x38], ecx
0074D1F5  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0074D1FA  C7 44 24 30 07 00 00 00         mov dword ptr [rsp + 0x30], 7
0074D202  F3 0F 7F 44 24 20               movdqu xmmword ptr [rsp + 0x20], xmm0
0074D208  E8 C3 6E 37 00                  call 0x140ac40d0
0074D20D  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
0074D212  48 33 CC                        xor rcx, rsp
0074D215  E8 26 F4 F5 FF                  call 0x1406ac640
0074D21A  48 83 C4 58                     add rsp, 0x58
0074D21E  C3                              ret
0074D21F  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall AlpcpLogConnectSuccess(int a1)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned int v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m38;

    v_rsp = (v_rsp) - (88);
    result = (*(unsigned __int64 *)(v_rip + 7067001)) ^ (v_rsp);
    v_stack_m18 = result;
    v_stack_m28 = v_xmm0;
    v_stack_m38 = v_xmm0;
    v_stack_m20 = a1;
    v_stack_m28 = 7;
    v_stack_m38 = v_xmm0;
    result = AlpcpInvokeLogCallbacks(v_stack_m38, 28, a3, a4);
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, 28, a3, a4);
    v_rsp = (v_rsp) + (88);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t AlpcpLogConnectSuccess(int32_t Arg1)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint32_t v_stack_m20;
    uint64_t v_stack_m28;
    uint64_t v_stack_m38;

    local_rsp = (local_rsp) - (88);
    result = (*(uint64_t *)(v_rip + 0x6BD579)) ^ (local_rsp);
    v_stack_m18 = result;
    v_stack_m28 = v_xmm0;
    v_stack_m38 = v_xmm0;
    v_stack_m20 = Arg1;
    v_stack_m28 = 7;
    v_stack_m38 = v_xmm0;
    result = AlpcpInvokeLogCallbacks(v_stack_m38, 28, a3, a4);
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, 28, a3, a4);
    local_rsp = (local_rsp) + (88);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0074D1BC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0074D1BC[BB_0074D1BC]
  bb_0074D21F[BB_0074D21F]
```
