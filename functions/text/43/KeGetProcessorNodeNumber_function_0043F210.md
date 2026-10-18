# KeGetProcessorNodeNumber

- RVA: `0x0043F210`–`0x0043F220` (길이 `16` bytes)
- VA: `0x000000014043F210`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `4`개 명령, `16/16` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **5**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [HvlInitializeProcessor](../../page/71/HvlInitializeProcessor_function_0071804C.md) at `0x007181D1`
- [PspAllocateThread](../../page/9E/PspAllocateThread_function_009EF72C.md) at `0x009EFFE8`
- [KiInitializeThreadCycleTable](../../pagelk/B6/KiInitializeThreadCycleTable_function_00B66B10.md) at `0x00B66B2F`
- [MmInitializeProcessor](../../pagelk/B7/MmInitializeProcessor_function_00B737F8.md) at `0x00B73827`
- [VmInitializeProcessor](../../pagelk/B7/VmInitializeProcessor_function_00B7E858.md) at `0x00B7E86E`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0043F210  48 8B 81 C0 00 00 00            mov rax, qword ptr [rcx + 0xc0]
0043F217  0F B7 80 8A 00 00 00            movzx eax, word ptr [rax + 0x8a]
0043F21E  C3                              ret
0043F21F  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KeGetProcessorNodeNumber(__int64 a1)
{
    return *(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 192) + 138);
}
```

## 5. (Beta) C Style

```c
int64_t KeGetProcessorNodeNumber(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    return *(uint16_t *)(*(uint64_t *)(arg1 + 0xC0) + 0x8A);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0xC0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0043F210&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0043F210[BB_0043F210]
  bb_0043F21F[BB_0043F21F]
```
