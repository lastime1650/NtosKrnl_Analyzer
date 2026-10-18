# MiGetEnclavePageList

- RVA: `0x004AEE58`–`0x004AEE86` (길이 `46` bytes)
- VA: `0x00000001404AEE58`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `14`개 명령, `46/46` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x004AEE64` → [MiPageToNode](../33/MiPageToNode_function_00338CD0.md) (function, `0x00338CD0`)

### Direct callers
- [MiInsertPageInList](../2B/MiInsertPageInList_function_002BA000.md) at `0x002BA9C1`
- [MxInsertEnclaveBootPages](../../init/C6/MxInsertEnclaveBootPages_function_00C68CB0.md) at `0x00C68EF8`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004AEE58  40 53                           push rbx
004AEE5A  48 83 EC 20                     sub rsp, 0x20
004AEE5E  48 8B D9                        mov rbx, rcx
004AEE61  48 8B CA                        mov rcx, rdx
004AEE64  E8 67 9E E8 FF                  call 0x140338cd0
004AEE69  8B D0                           mov edx, eax
004AEE6B  48 8B 43 10                     mov rax, qword ptr [rbx + 0x10]
004AEE6F  4C 69 C2 80 DF 00 00            imul r8, rdx, 0xdf80
004AEE76  48 05 C0 DE 00 00               add rax, 0xdec0
004AEE7C  49 03 C0                        add rax, r8
004AEE7F  48 83 C4 20                     add rsp, 0x20
004AEE83  5B                              pop rbx
004AEE84  C3                              ret
004AEE85  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiGetEnclavePageList(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    result = MiPageToNode(a2, a2, a3, a4);
    a3 = (a3) * ((unsigned int)((unsigned int)(result)));
    result = (*(unsigned __int64 *)(a1 + 16)) + (0xDEC0ULL);
    result = (result) + (a3);
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MiGetEnclavePageList(void *Arg1, int64_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    result = MiPageToNode(Arg2, Arg2, a3, a4);
    a3 = (a3) * ((uint32_t)((uint32_t)(result)));
    result = (*(uint64_t *)(arg1 + 0x10)) + (0xDEC0ULL);
    result = (result) + (a3);
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x10` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004AEE58&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004AEE58[BB_004AEE58]
  bb_004AEE85[BB_004AEE85]
```
