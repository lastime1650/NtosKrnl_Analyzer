# VslCreateSecureAllocation

- RVA: `0x004BD7D0`–`0x004BD84E` (길이 `126` bytes)
- VA: `0x00000001404BD7D0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BC090`
- 디코드: `31`개 명령, `126/126` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x004BD800` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x004BD819` → [VslpEnterIumSecureMode](../23/VslpEnterIumSecureMode_function_00235E50.md) (function, `0x00235E50`)
- `0x004BD82D` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x004BD7DD` → RVA `0x00E0A740` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004BD7D0  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
004BD7D5  57                              push rdi
004BD7D6  48 81 EC A0 00 00 00            sub rsp, 0xa0
004BD7DD  48 8B 05 5C CF 94 00            mov rax, qword ptr [rip + 0x94cf5c]
004BD7E4  48 33 C4                        xor rax, rsp
004BD7E7  48 89 84 24 90 00 00 00         mov qword ptr [rsp + 0x90], rax
004BD7EF  48 8B FA                        mov rdi, rdx
004BD7F2  48 8B D9                        mov rbx, rcx
004BD7F5  33 D2                           xor edx, edx
004BD7F7  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
004BD7FC  44 8D 42 68                     lea r8d, [rdx + 0x68]
004BD800  E8 3B 94 20 00                  call 0x1406c6c40
004BD805  BA 16 00 00 00                  mov edx, 0x16
004BD80A  48 89 5C 24 28                  mov qword ptr [rsp + 0x28], rbx
004BD80F  4C 8D 4C 24 20                  lea r9, [rsp + 0x20]
004BD814  45 33 C0                        xor r8d, r8d
004BD817  B1 02                           mov cl, 2
004BD819  E8 32 86 D7 FF                  call 0x140235e50
004BD81E  85 C0                           test eax, eax
004BD820  79 22                           jns 0x1404bd844
004BD822  48 8B 8C 24 90 00 00 00         mov rcx, qword ptr [rsp + 0x90]
004BD82A  48 33 CC                        xor rcx, rsp
004BD82D  E8 0E EE 1E 00                  call 0x1406ac640
004BD832  48 8B 9C 24 B0 00 00 00         mov rbx, qword ptr [rsp + 0xb0]
004BD83A  48 81 C4 A0 00 00 00            add rsp, 0xa0
004BD841  5F                              pop rdi
004BD842  C3                              ret
004BD843  CC                              int3
004BD844  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
004BD849  48 89 0F                        mov qword ptr [rdi], rcx
004BD84C  EB D4                           jmp 0x1404bd822
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall VslCreateSecureAllocation(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (160);
    result = (*(unsigned __int64 *)(v_rip + 9752412)) ^ (v_rsp);
    v_stack_m18 = result;
    a2 = 0;
    result = memset(v_stack_m88, a2, a2 + 104, a4);
    v_stack_m80 = a1;
    a3 = 0;
    result = VslpEnterIumSecureMode(2, 22, a3, v_stack_m88);
    if (!sign_flag) goto loc_004BD844;
loc_004BD822:
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, 22, a3, v_stack_m88);
    v_rsp = (v_rsp) + (160);
    return result;
loc_004BD844:
    *(unsigned __int64 *)(a2) = v_stack_p30;
    goto loc_004BD822;
}
```

## 5. (Beta) C Style

```c
int64_t VslCreateSecureAllocation(int64_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_p30;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (160);
    result = (*(uint64_t *)(v_rip + 0x94CF5C)) ^ (local_rsp);
    v_stack_m18 = result;
    Arg2 = 0;
    result = memset(v_stack_m88, Arg2, Arg2 + 104, a4);
    v_stack_m80 = Arg1;
    a3 = 0;
    result = VslpEnterIumSecureMode(2, 22, a3, v_stack_m88);
    if (!sign_flag) goto loc_004BD844;
loc_004BD822:
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, 22, a3, v_stack_m88);
    local_rsp = (local_rsp) + (160);
    return result;
loc_004BD844:
    *(uint64_t *)(arg2) = v_stack_p30;
    goto loc_004BD822;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004BD7D0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004BD7D0[BB_004BD7D0]
  bb_004BD822[BB_004BD822]
  bb_004BD843[BB_004BD843]
  bb_004BD844[BB_004BD844]
  bb_004BD7D0 -->|branch| bb_004BD844
  bb_004BD7D0 -->|fallthrough| bb_004BD822
  bb_004BD843 -->|flow| bb_004BD844
  bb_004BD844 -->|branch| bb_004BD822
```
