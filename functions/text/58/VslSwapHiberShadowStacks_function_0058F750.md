# VslSwapHiberShadowStacks

- RVA: `0x0058F750`–`0x0058F7BA` (길이 `106` bytes)
- VA: `0x000000014058F750`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000AF554`
- 디코드: `25`개 명령, `106/106` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x0058F779` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0058F79B` → [VslpEnterIumSecureMode](../23/VslpEnterIumSecureMode_function_00235E50.md) (function, `0x00235E50`)
- `0x0058F7AB` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [PopSaveHiberContextWrapper](../6B/PopSaveHiberContextWrapper_function_006BA360.md) at `0x006BA36F`
- [PopSaveHiberContextWrapper](../6B/PopSaveHiberContextWrapper_function_006BA360.md) at `0x006BA3CA`

### Static image references
- `0x0058F759` → RVA `0x00E0A740` (`.data`; read)
- `0x0058F77E` → RVA `0x01201841` (`CFGRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0058F750  40 53                           push rbx
0058F752  48 81 EC A0 00 00 00            sub rsp, 0xa0
0058F759  48 8B 05 E0 AF 87 00            mov rax, qword ptr [rip + 0x87afe0]
0058F760  48 33 C4                        xor rax, rsp
0058F763  48 89 84 24 90 00 00 00         mov qword ptr [rsp + 0x90], rax
0058F76B  33 D2                           xor edx, edx
0058F76D  48 8B D9                        mov rbx, rcx
0058F770  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0058F775  44 8D 42 68                     lea r8d, [rdx + 0x68]
0058F779  E8 C2 74 13 00                  call 0x1406c6c40
0058F77E  80 3D BC 20 C7 00 00            cmp byte ptr [rip + 0xc720bc], 0
0058F785  74 19                           je 0x14058f7a0
0058F787  BA 09 01 00 00                  mov edx, 0x109
0058F78C  48 89 5C 24 28                  mov qword ptr [rsp + 0x28], rbx
0058F791  4C 8D 4C 24 20                  lea r9, [rsp + 0x20]
0058F796  45 33 C0                        xor r8d, r8d
0058F799  B1 02                           mov cl, 2
0058F79B  E8 B0 66 CA FF                  call 0x140235e50
0058F7A0  48 8B 8C 24 90 00 00 00         mov rcx, qword ptr [rsp + 0x90]
0058F7A8  48 33 CC                        xor rcx, rsp
0058F7AB  E8 90 CE 11 00                  call 0x1406ac640
0058F7B0  48 81 C4 A0 00 00 00            add rsp, 0xa0
0058F7B7  5B                              pop rbx
0058F7B8  C3                              ret
0058F7B9  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall VslSwapHiberShadowStacks(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;

    v_rsp = (v_rsp) - (160);
    result = (*(unsigned __int64 *)(v_rip + 8892384)) ^ (v_rsp);
    v_stack_m18 = result;
    a2 = 0;
    result = memset(v_stack_m88, a2, a2 + 104, a4);
    if ((*(unsigned __int8 *)(v_rip + 13050044)) != 0) {
        a2 = 265;
        v_stack_m80 = a1;
        a4 = v_stack_m88;
        a3 = 0;
        a1 = 2;
        result = VslpEnterIumSecureMode(a1, a2, a3, a4);
    }
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (160);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t VslSwapHiberShadowStacks(int64_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;

    local_rsp = (local_rsp) - (160);
    result = (*(uint64_t *)(v_rip + 0x87AFE0)) ^ (local_rsp);
    v_stack_m18 = result;
    Arg2 = 0;
    result = memset(v_stack_m88, Arg2, Arg2 + 104, a4);
    if ((*(uint8_t *)(v_rip + 0xC720BC)) != 0) {
        Arg2 = 265;
        v_stack_m80 = Arg1;
        a4 = v_stack_m88;
        a3 = 0;
        Arg1 = 2;
        result = VslpEnterIumSecureMode(Arg1, Arg2, a3, a4);
    }
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, a3, a4);
    local_rsp = (local_rsp) + (160);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0058F750&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0058F750[BB_0058F750]
  bb_0058F787[BB_0058F787]
  bb_0058F7A0[BB_0058F7A0]
  bb_0058F7B9[BB_0058F7B9]
  bb_0058F750 -->|branch| bb_0058F7A0
  bb_0058F750 -->|fallthrough| bb_0058F787
  bb_0058F787 -->|flow| bb_0058F7A0
```
