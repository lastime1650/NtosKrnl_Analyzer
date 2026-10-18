# MiReadEntirePageHashEntry

- RVA: `0x0046A494`–`0x0046A4B8` (길이 `36` bytes)
- VA: `0x000000014046A494`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `13`개 명령, `36/36` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [MiLateWritePageHash](../4D/MiLateWritePageHash_function_004D4148.md) at `0x004D41C8`

### Static image references
- `0x0046A49A` → RVA `0x00E37390` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0046A494  8B 01                           mov eax, dword ptr [rcx]
0046A496  89 02                           mov dword ptr [rdx], eax
0046A498  33 C0                           xor eax, eax
0046A49A  39 05 F0 CE 9C 00               cmp dword ptr [rip + 0x9ccef0], eax
0046A4A0  75 09                           jne 0x14046a4ab
0046A4A2  48 89 42 08                     mov qword ptr [rdx + 8], rax
0046A4A6  89 42 04                        mov dword ptr [rdx + 4], eax
0046A4A9  C3                              ret
0046A4AA  CC                              int3
0046A4AB  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
0046A4AF  48 89 42 08                     mov qword ptr [rdx + 8], rax
0046A4B3  8B 41 04                        mov eax, dword ptr [rcx + 4]
0046A4B6  EB EE                           jmp 0x14046a4a6
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiReadEntirePageHashEntry(__int64 a1, __int64 a2)
{
    __int64 result;

    *(unsigned int *)(a2) = (unsigned int)((unsigned int)(*(unsigned int *)(a1)));
    result = 0;
    if ((*(unsigned int *)(v_rip + 10276592)) != 0) goto loc_0046A4AB;
    *(unsigned __int64 *)(a2 + 8) = 0;
loc_0046A4A6:
    *(unsigned int *)(a2 + 4) = 0;
    return result;
loc_0046A4AB:
    *(unsigned __int64 *)(a2 + 8) = *(unsigned __int64 *)(a1 + 8);
    goto loc_0046A4A6;
}
```

## 5. (Beta) C Style

```c
int64_t MiReadEntirePageHashEntry(void *Arg1, void *Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;

    *(uint32_t *)(arg2) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1)));
    result = 0;
    if ((*(uint32_t *)(v_rip + 0x9CCEF0)) != 0) goto loc_0046A4AB;
    *(uint64_t *)(arg2 + 0x8) = 0;
loc_0046A4A6:
    *(uint32_t *)(arg2 + 0x4) = 0;
    return result;
loc_0046A4AB:
    *(uint64_t *)(arg2 + 0x8) = *(uint64_t *)(arg1 + 0x8);
    goto loc_0046A4A6;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg1` | `+ 0x4` | `32` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg2` | `+ 0x0` | `32` | `W` |
| `Arg2` | `+ 0x4` | `32` | `W` |
| `Arg2` | `+ 0x8` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0046A494&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0046A494[BB_0046A494]
  bb_0046A4A2[BB_0046A4A2]
  bb_0046A4A6[BB_0046A4A6]
  bb_0046A4AA[BB_0046A4AA]
  bb_0046A4AB[BB_0046A4AB]
  bb_0046A494 -->|branch| bb_0046A4AB
  bb_0046A494 -->|fallthrough| bb_0046A4A2
  bb_0046A4A2 -->|flow| bb_0046A4A6
  bb_0046A4AA -->|flow| bb_0046A4AB
  bb_0046A4AB -->|branch| bb_0046A4A6
```
