# MiDecommitHandleValidPte

- RVA: `0x00241A50`–`0x00241A6E` (길이 `30` bytes)
- VA: `0x0000000140241A50`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00061888`
- 디코드: `8`개 명령, `30/30` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [MiDeleteEmptyPageTableWorker](../47/MiDeleteEmptyPageTableWorker_function_0047FE18.md) at `0x0047FF21`
- [MiStoreDiscardPoisonedPage](../69/MiStoreDiscardPoisonedPage_function_00692858.md) at `0x00692BD5`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x00241A68` → [sub_00241B5E](Unknown_function_00241B5E.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00241A50  48 89 5C 24 18                  mov qword ptr [rsp + 0x18], rbx
00241A55  57                              push rdi
00241A56  48 83 EC 20                     sub rsp, 0x20
00241A5A  8B 81 9C 00 00 00               mov eax, dword ptr [rcx + 0x9c]
00241A60  48 8B DA                        mov rbx, rdx
00241A63  48 8B F9                        mov rdi, rcx
00241A66  A8 08                           test al, 8
00241A68  0F 85 F0 00 00 00               jne 0x140241b5e
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiDecommitHandleValidPte(__int64 a1, __int64 a2)
{
    __int64 v_rsp;
    unsigned __int64 v_stack_p18;

    v_stack_p18 = v_rbx;
    v_rsp = (v_rsp) - (32);
}
```

## 5. (Beta) C Style

```c
int64_t MiDecommitHandleValidPte(void *Arg1, int64_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t local_rsp;
    uint64_t v_stack_p18;

    v_stack_p18 = local_rbx;
    local_rsp = (local_rsp) - (32);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x9C` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00241A50&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00241A50[BB_00241A50]
```
