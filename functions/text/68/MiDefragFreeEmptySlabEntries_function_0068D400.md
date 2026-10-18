# MiDefragFreeEmptySlabEntries

- RVA: `0x0068D400`–`0x0068D434` (길이 `52` bytes)
- VA: `0x000000014068D400`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CAAC`
- 디코드: `16`개 명령, `52/52` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0068D417` → [MiFreeSlabEntries](../2D/MiFreeSlabEntries_function_002DAFC0.md) (function, `0x002DAFC0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0068D400  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
0068D405  57                              push rdi
0068D406  48 83 EC 20                     sub rsp, 0x20
0068D40A  48 8B 5A 78                     mov rbx, qword ptr [rdx + 0x78]
0068D40E  41 B8 02 00 00 00               mov r8d, 2
0068D414  48 8B FA                        mov rdi, rdx
0068D417  E8 A4 DB C4 FF                  call 0x1402dafc0
0068D41C  48 8B 4F 78                     mov rcx, qword ptr [rdi + 0x78]
0068D420  33 C0                           xor eax, eax
0068D422  48 3B D9                        cmp rbx, rcx
0068D425  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
0068D42A  0F 97 C0                        seta al
0068D42D  48 83 C4 20                     add rsp, 0x20
0068D431  5F                              pop rdi
0068D432  C3                              ret
0068D433  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiDefragFreeEmptySlabEntries(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    result = MiFreeSlabEntries(a1, a2, 2, a4);
    result = 0;
    result = ((*(unsigned __int64 *)(a2 + 120)) > (*(unsigned __int64 *)(a2 + 120))) ? 1 : 0;
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MiDefragFreeEmptySlabEntries(int64_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    result = MiFreeSlabEntries(Arg1, Arg2, 2, a4);
    result = 0;
    result = ((*(uint64_t *)(arg2 + 0x78)) > (*(uint64_t *)(arg2 + 0x78))) ? 1 : 0;
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x78` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0068D400&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0068D400[BB_0068D400]
  bb_0068D433[BB_0068D433]
```
