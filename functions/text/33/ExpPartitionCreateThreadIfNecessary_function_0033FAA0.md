# ExpPartitionCreateThreadIfNecessary

- RVA: `0x0033FAA0`–`0x0033FADD` (길이 `61` bytes)
- VA: `0x000000014033FAA0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `18`개 명령, `61/61` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0033FAB4` → [ExpNewThreadNecessary](ExpNewThreadNecessary_function_0033FAF0.md) (function, `0x0033FAF0`)
- `0x0033FAD2` → [KeSetEvent](KeSetEvent_function_0033F310.md) (function, `0x0033F310`)

### Direct callers
- [ExpTryQueueWorkItem](../39/ExpTryQueueWorkItem_function_0039801C.md) at `0x0039817B`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0033FAA0  48 83 EC 28                     sub rsp, 0x28
0033FAA4  4C 8B D1                        mov r10, rcx
0033FAA7  4C 8B DA                        mov r11, rdx
0033FAAA  41 8B 90 D4 02 00 00            mov edx, dword ptr [r8 + 0x2d4]
0033FAB1  49 8B C8                        mov rcx, r8
0033FAB4  E8 37 00 00 00                  call 0x14033faf0
0033FAB9  84 C0                           test al, al
0033FABB  74 1A                           je 0x14033fad7
0033FABD  41 0F B7 0B                     movzx ecx, word ptr [r11]
0033FAC1  45 33 C0                        xor r8d, r8d
0033FAC4  49 8B 42 10                     mov rax, qword ptr [r10 + 0x10]
0033FAC8  33 D2                           xor edx, edx
0033FACA  48 8B 0C C8                     mov rcx, qword ptr [rax + rcx*8]
0033FACE  48 83 C1 10                     add rcx, 0x10
0033FAD2  E8 39 F8 FF FF                  call 0x14033f310
0033FAD7  48 83 C4 28                     add rsp, 0x28
0033FADB  C3                              ret
0033FADC  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ExpPartitionCreateThreadIfNecessary(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = ExpNewThreadNecessary(a3, (unsigned int)(*(unsigned int *)(a3 + 724)), a3, a4);
    if ((unsigned __int8)(result) != 0) {
        a1 = *(unsigned __int16 *)(a2);
        a3 = 0;
        result = *(unsigned __int64 *)(a1 + 16);
        a2 = 0;
        a1 = *(unsigned __int64 *)(result + a1 * 8);
        a1 = (a1) + (16);
        result = KeSetEvent(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t ExpPartitionCreateThreadIfNecessary(int64_t Arg1, int64_t Arg2, void *Arg3)
{
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = ExpNewThreadNecessary(Arg3, (uint32_t)(*(uint32_t *)(arg3 + 0x2D4)), Arg3, a4);
    if ((uint8_t)(result) != 0) {
        Arg1 = *(uint16_t *)(Arg2);
        Arg3 = 0;
        result = *(uint64_t *)(Arg1 + 0x10);
        Arg2 = 0;
        Arg1 = *(uint64_t *)(result + Arg1 * 8);
        Arg1 = (Arg1) + (16);
        result = KeSetEvent(Arg1, Arg2, Arg3, a4);
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg3` | `+ 0x2D4` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0033FAA0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0033FAA0[BB_0033FAA0]
  bb_0033FABD[BB_0033FABD]
  bb_0033FAD7[BB_0033FAD7]
  bb_0033FADC[BB_0033FADC]
  bb_0033FAA0 -->|branch| bb_0033FAD7
  bb_0033FAA0 -->|fallthrough| bb_0033FABD
  bb_0033FABD -->|flow| bb_0033FAD7
```
