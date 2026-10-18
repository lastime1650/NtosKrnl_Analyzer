# MiGetUserReservationHighestAddress

- RVA: `0x00982430`–`0x0098246E` (길이 `62` bytes)
- VA: `0x0000000140982430`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `17`개 명령, `62/62` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [MiMapImageInSystemProcess](../7F/MiMapImageInSystemProcess_function_007FE4F8.md) at `0x007FE594`
- [MiAllocateEnclaveVad](../80/MiAllocateEnclaveVad_function_008080A4.md) at `0x008082A6`
- [MiAllocateNewSubAllocatedRegion](MiAllocateNewSubAllocatedRegion_function_00981EC0.md) at `0x00981F4B`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00982430  4C 8B C9                        mov r9, rcx
00982433  49 B8 FF FF FE FF FF 7F 00 00   movabs r8, 0x7ffffffeffff
0098243D  48 85 D2                        test rdx, rdx
00982440  75 13                           jne 0x140982455
00982442  49 8B 81 68 03 00 00            mov rax, qword ptr [r9 + 0x368]
00982449  48 FF C8                        dec rax
0098244C  4C 3B C0                        cmp r8, rax
0098244F  49 0F 46 C0                     cmovbe rax, r8
00982453  C3                              ret
00982454  CC                              int3
00982455  48 C7 C0 FF FF FF FF            mov rax, 0xffffffffffffffff
0098245C  48 8B CA                        mov rcx, rdx
0098245F  48 D3 E8                        shr rax, cl
00982462  49 3B C0                        cmp rax, r8
00982465  49 0F 47 C0                     cmova rax, r8
00982469  4C 8B C0                        mov r8, rax
0098246C  EB D4                           jmp 0x140982442
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiGetUserReservationHighestAddress(__int64 a1, __int64 a2)
{
    __int64 result;

    if (a2 != 0) goto loc_00982455;
loc_00982442:
    result = (*(unsigned __int64 *)(a1 + 872)) - 1;
    if (a3 <= result) { result = a3; }
    return result;
loc_00982455:
    result = (-1) >> ((unsigned __int8)(a2));
    if (result > a3) { result = a3; }
    goto loc_00982442;
}
```

## 5. (Beta) C Style

```c
int64_t MiGetUserReservationHighestAddress(void *Arg1, int64_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;

    if (Arg2 != 0) goto loc_00982455;
loc_00982442:
    result = (*(uint64_t *)(arg1 + 0x368)) - 1;
    if (a3 <= result) { result = a3; }
    return result;
loc_00982455:
    result = (-1) >> ((uint8_t)(Arg2));
    if (result > a3) { result = a3; }
    goto loc_00982442;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x368` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00982430&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00982430[BB_00982430]
  bb_00982442[BB_00982442]
  bb_00982454[BB_00982454]
  bb_00982455[BB_00982455]
  bb_00982430 -->|branch| bb_00982455
  bb_00982430 -->|fallthrough| bb_00982442
  bb_00982454 -->|flow| bb_00982455
  bb_00982455 -->|branch| bb_00982442
```
