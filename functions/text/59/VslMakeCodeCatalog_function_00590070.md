# VslMakeCodeCatalog

- RVA: `0x00590070`–`0x005900F4` (길이 `132` bytes)
- VA: `0x0000000140590070`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C6C70`
- 디코드: `32`개 명령, `132/132` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x005900A0` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x005900C1` → [VslpEnterIumSecureMode](../23/VslpEnterIumSecureMode_function_00235E50.md) (function, `0x00235E50`)
- `0x005900DD` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0059007D` → RVA `0x00E0A740` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00590070  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
00590075  57                              push rdi
00590076  48 81 EC A0 00 00 00            sub rsp, 0xa0
0059007D  48 8B 05 BC A6 87 00            mov rax, qword ptr [rip + 0x87a6bc]
00590084  48 33 C4                        xor rax, rsp
00590087  48 89 84 24 90 00 00 00         mov qword ptr [rsp + 0x90], rax
0059008F  48 8B DA                        mov rbx, rdx
00590092  48 8B F9                        mov rdi, rcx
00590095  33 D2                           xor edx, edx
00590097  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0059009C  44 8D 42 68                     lea r8d, [rdx + 0x68]
005900A0  E8 9B 6B 13 00                  call 0x1406c6c40
005900A5  48 8B 07                        mov rax, qword ptr [rdi]
005900A8  4C 8D 4C 24 20                  lea r9, [rsp + 0x20]
005900AD  BA 18 00 00 00                  mov edx, 0x18
005900B2  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
005900B7  45 33 C0                        xor r8d, r8d
005900BA  48 89 5C 24 30                  mov qword ptr [rsp + 0x30], rbx
005900BF  B1 02                           mov cl, 2
005900C1  E8 8A 5D CA FF                  call 0x140235e50
005900C6  85 C0                           test eax, eax
005900C8  78 08                           js 0x1405900d2
005900CA  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
005900CF  48 89 0F                        mov qword ptr [rdi], rcx
005900D2  48 8B 8C 24 90 00 00 00         mov rcx, qword ptr [rsp + 0x90]
005900DA  48 33 CC                        xor rcx, rsp
005900DD  E8 5E C5 11 00                  call 0x1406ac640
005900E2  48 8B 9C 24 B8 00 00 00         mov rbx, qword ptr [rsp + 0xb8]
005900EA  48 81 C4 A0 00 00 00            add rsp, 0xa0
005900F1  5F                              pop rdi
005900F2  C3                              ret
005900F3  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall VslMakeCodeCatalog(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_p10;

    v_stack_p10 = v_rbx;
    v_rsp = (v_rsp) - (160);
    result = (*(unsigned __int64 *)(v_rip + 8890044)) ^ (v_rsp);
    v_stack_m18 = result;
    a2 = 0;
    result = memset(v_stack_m88, a2, a2 + 104, a4);
    v_stack_m80 = *(unsigned __int64 *)(a1);
    a3 = 0;
    v_stack_m78 = 0;
    result = VslpEnterIumSecureMode(2, 24, a3, v_stack_m88);
    if (!(sign_flag)) {
        a1 = v_stack_m78;
        *(unsigned __int64 *)(a1) = a1;
    }
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, 24, a3, v_stack_m88);
    v_rsp = (v_rsp) + (160);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t VslMakeCodeCatalog(void *Arg1, int64_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_p10;

    v_stack_p10 = local_rbx;
    local_rsp = (local_rsp) - (160);
    result = (*(uint64_t *)(v_rip + 0x87A6BC)) ^ (local_rsp);
    v_stack_m18 = result;
    Arg2 = 0;
    result = memset(v_stack_m88, Arg2, Arg2 + 104, a4);
    v_stack_m80 = *(uint64_t *)(arg1);
    a3 = 0;
    v_stack_m78 = 0;
    result = VslpEnterIumSecureMode(2, 24, a3, v_stack_m88);
    if (!(sign_flag)) {
        Arg1 = v_stack_m78;
        *(void **)(arg1) = Arg1;
    }
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, 24, a3, v_stack_m88);
    local_rsp = (local_rsp) + (160);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00590070&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00590070[BB_00590070]
  bb_005900CA[BB_005900CA]
  bb_005900D2[BB_005900D2]
  bb_005900F3[BB_005900F3]
  bb_00590070 -->|branch| bb_005900D2
  bb_00590070 -->|fallthrough| bb_005900CA
  bb_005900CA -->|flow| bb_005900D2
```
