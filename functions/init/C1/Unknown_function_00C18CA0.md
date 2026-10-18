# sub_00C18CA0

- RVA: `0x00C18CA0`–`0x00C18CCC` (길이 `44` bytes)
- VA: `0x0000000140C18CA0`
- 실행 섹션: `INIT`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00064C80`
- 디코드: `15`개 명령, `44/44` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00C18CBD` → [sub_00BF16D0](../BF/Unknown_function_00BF16D0.md) (function, `0x00BF16D0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00C18CA0  40 53                           push rbx
00C18CA2  48 83 EC 30                     sub rsp, 0x30
00C18CA6  8B 41 18                        mov eax, dword ptr [rcx + 0x18]
00C18CA9  48 8B D9                        mov rbx, rcx
00C18CAC  4C 8B 49 10                     mov r9, qword ptr [rcx + 0x10]
00C18CB0  44 8B 41 08                     mov r8d, dword ptr [rcx + 8]
00C18CB4  8B 51 04                        mov edx, dword ptr [rcx + 4]
00C18CB7  8B 09                           mov ecx, dword ptr [rcx]
00C18CB9  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
00C18CBD  E8 0E 8A FD FF                  call 0x140bf16d0
00C18CC2  88 43 1C                        mov byte ptr [rbx + 0x1c], al
00C18CC5  48 83 C4 30                     add rsp, 0x30
00C18CC9  5B                              pop rbx
00C18CCA  C3                              ret
00C18CCB  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00C18CA0(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;
    unsigned int v_stack_m18;

    v_rsp = (v_rsp) - (48);
    v_stack_m18 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 24)));
    result = sub_00BF16D0((unsigned int)(*(unsigned int *)(a1)), (unsigned int)(*(unsigned int *)(a1 + 4)), (unsigned int)(*(unsigned int *)(a1 + 8)), *(unsigned __int64 *)(a1 + 16));
    *(unsigned __int8 *)(a1 + 28) = (unsigned __int8)(result);
    v_rsp = (v_rsp) + (48);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t sub_00C18CA0(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint32_t v_stack_m18;

    local_rsp = (local_rsp) - (48);
    v_stack_m18 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x18)));
    result = sub_00BF16D0((uint32_t)(*(uint32_t *)(arg1)), (uint32_t)(*(uint32_t *)(arg1 + 0x4)), (uint32_t)(*(uint32_t *)(arg1 + 0x8)), *(uint64_t *)(arg1 + 0x10));
    *(uint8_t *)(arg1 + 0x1C) = (uint8_t)(result);
    local_rsp = (local_rsp) + (48);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg1` | `+ 0x4` | `32` | `R` |
| `Arg1` | `+ 0x8` | `32` | `R` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x18` | `32` | `R` |
| `Arg1` | `+ 0x1C` | `8` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=init&rva=0x00C18CA0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00C18CA0[BB_00C18CA0]
  bb_00C18CCB[BB_00C18CCB]
```
