# CmEnumerateKeyCallout

- RVA: `0x0084C560`–`0x0084C5A0` (길이 `64` bytes)
- VA: `0x000000014084C560`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000697A4`
- 디코드: `19`개 명령, `64/64` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0084C592` → [CmEnumerateKey](CmEnumerateKey_function_0084E490.md) (function, `0x0084E490`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0084C560  40 53                           push rbx
0084C562  48 83 EC 40                     sub rsp, 0x40
0084C566  48 8B 41 30                     mov rax, qword ptr [rcx + 0x30]
0084C56A  48 8B D9                        mov rbx, rcx
0084C56D  44 8B 49 1C                     mov r9d, dword ptr [rcx + 0x1c]
0084C571  44 8B 41 18                     mov r8d, dword ptr [rcx + 0x18]
0084C575  48 8B 51 10                     mov rdx, qword ptr [rcx + 0x10]
0084C579  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0084C57E  8B 41 28                        mov eax, dword ptr [rcx + 0x28]
0084C581  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
0084C585  48 8B 41 20                     mov rax, qword ptr [rcx + 0x20]
0084C589  48 8B 49 08                     mov rcx, qword ptr [rcx + 8]
0084C58D  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0084C592  E8 F9 1E 00 00                  call 0x14084e490
0084C597  89 03                           mov dword ptr [rbx], eax
0084C599  48 83 C4 40                     add rsp, 0x40
0084C59D  5B                              pop rbx
0084C59E  C3                              ret
0084C59F  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmEnumerateKeyCallout(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned int v_stack_m20;
    unsigned __int64 v_stack_m28;

    v_rsp = (v_rsp) - (64);
    v_stack_m18 = *(unsigned __int64 *)(a1 + 48);
    v_stack_m20 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 40)));
    v_stack_m28 = *(unsigned __int64 *)(a1 + 32);
    result = CmEnumerateKey(*(unsigned __int64 *)(a1 + 8), *(unsigned __int64 *)(a1 + 16), (unsigned int)(*(unsigned int *)(a1 + 24)), (unsigned int)(*(unsigned int *)(a1 + 28)));
    *(unsigned int *)(a1) = (unsigned int)(result);
    v_rsp = (v_rsp) + (64);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t CmEnumerateKeyCallout(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint32_t v_stack_m20;
    uint64_t v_stack_m28;

    local_rsp = (local_rsp) - (64);
    v_stack_m18 = *(uint64_t *)(arg1 + 0x30);
    v_stack_m20 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x28)));
    v_stack_m28 = *(uint64_t *)(arg1 + 0x20);
    result = CmEnumerateKey(*(uint64_t *)(arg1 + 0x8), *(uint64_t *)(arg1 + 0x10), (uint32_t)(*(uint32_t *)(arg1 + 0x18)), (uint32_t)(*(uint32_t *)(arg1 + 0x1C)));
    *(uint32_t *)(arg1) = (uint32_t)(result);
    local_rsp = (local_rsp) + (64);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `W` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x18` | `32` | `R` |
| `Arg1` | `+ 0x1C` | `32` | `R` |
| `Arg1` | `+ 0x20` | `64` | `R` |
| `Arg1` | `+ 0x28` | `32` | `R` |
| `Arg1` | `+ 0x30` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0084C560&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0084C560[BB_0084C560]
  bb_0084C59F[BB_0084C59F]
```
