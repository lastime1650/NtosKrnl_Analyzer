# AlpcpCreatePort

- RVA: `0x009E7358`–`0x009E73B5` (길이 `93` bytes)
- VA: `0x00000001409E7358`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00089EA4`
- 디코드: `27`개 명령, `93/93` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x009E738C` → [ObCreateObjectEx](../89/ObCreateObjectEx_function_0089B1E0.md) (function, `0x0089B1E0`)
- `0x009E73A2` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)

### Direct callers
- [AlpcpCreateConnectionPort](AlpcpCreateConnectionPort_function_009E70B0.md) at `0x009E712C`
- [AlpcpAcceptConnectPort](../A3/AlpcpAcceptConnectPort_function_00A34290.md) at `0x00A34906`

### Static image references
- `0x009E737E` → RVA `0x00FC6C18` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x009E73A2` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
009E7358  48 8B C4                        mov rax, rsp
009E735B  48 89 58 08                     mov qword ptr [rax + 8], rbx
009E735F  57                              push rdi
009E7360  48 83 EC 50                     sub rsp, 0x50
009E7364  48 83 60 F0 00                  and qword ptr [rax - 0x10], 0
009E7369  49 8B F8                        mov rdi, r8
009E736C  48 89 78 E8                     mov qword ptr [rax - 0x18], rdi
009E7370  4C 8B C2                        mov r8, rdx
009E7373  83 60 E0 00                     and dword ptr [rax - 0x20], 0
009E7377  44 8A C9                        mov r9b, cl
009E737A  83 60 D8 00                     and dword ptr [rax - 0x28], 0
009E737E  48 8B 15 93 F8 5D 00            mov rdx, qword ptr [rip + 0x5df893]
009E7385  C7 40 D0 D8 01 00 00            mov dword ptr [rax - 0x30], 0x1d8
009E738C  E8 4F 3E EB FF                  call 0x14089b1e0
009E7391  8B D8                           mov ebx, eax
009E7393  85 C0                           test eax, eax
009E7395  78 10                           js 0x1409e73a7
009E7397  48 8B 0F                        mov rcx, qword ptr [rdi]
009E739A  33 D2                           xor edx, edx
009E739C  41 B8 D8 01 00 00               mov r8d, 0x1d8
009E73A2  E8 99 F8 CD FF                  call 0x1406c6c40
009E73A7  8B C3                           mov eax, ebx
009E73A9  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
009E73AE  48 83 C4 50                     add rsp, 0x50
009E73B2  5F                              pop rdi
009E73B3  C3                              ret
009E73B4  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall AlpcpCreatePort(unsigned __int8 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    v_rsp = (v_rsp) - (80);
    *(unsigned __int64 *)(v_rsp - 24) = a3;
    *(unsigned int *)(v_rsp - 48) = 472;
    result = ObCreateObjectEx(a1, *(unsigned __int64 *)(v_rip + 6158483), a2, a1);
    if (!(sign_flag)) {
        a1 = *(unsigned __int64 *)(a3);
        a2 = 0;
        a3 = 472;
        result = memset(a1, a2, a3, a1);
    }
    v_rsp = (v_rsp) + (80);
    return (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))));
}
```

## 5. (Beta) C Style

```c
int64_t AlpcpCreatePort(uint8_t Arg1, int64_t Arg2, void *Arg3)
{
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    local_rsp = (local_rsp) - (80);
    *(void **)(local_rsp - 0x18) = Arg3;
    *(uint32_t *)(local_rsp - 0x30) = 472;
    result = ObCreateObjectEx(Arg1, *(uint64_t *)(v_rip + 0x5DF893), Arg2, Arg1);
    if (!(sign_flag)) {
        Arg1 = *(uint64_t *)(arg3);
        Arg2 = 0;
        Arg3 = 472;
        result = memset(Arg1, Arg2, Arg3, Arg1);
    }
    local_rsp = (local_rsp) + (80);
    return (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg3` | `+ 0x0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009E7358&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_009E7358[BB_009E7358]
  bb_009E7397[BB_009E7397]
  bb_009E73A7[BB_009E73A7]
  bb_009E73B4[BB_009E73B4]
  bb_009E7358 -->|branch| bb_009E73A7
  bb_009E7358 -->|fallthrough| bb_009E7397
  bb_009E7397 -->|flow| bb_009E73A7
```
