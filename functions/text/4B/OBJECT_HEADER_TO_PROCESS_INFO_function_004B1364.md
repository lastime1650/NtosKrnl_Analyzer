# OBJECT_HEADER_TO_PROCESS_INFO

- RVA: `0x004B1364`–`0x004B1386` (길이 `34` bytes)
- VA: `0x00000001404B1364`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `12`개 명령, `34/34` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [ObpIncrementHandleCountEx](../../page/86/ObpIncrementHandleCountEx_function_0086DA10.md) at `0x0086E254`
- [ObpIncrementHandleCountEx](../../page/86/ObpIncrementHandleCountEx_function_0086DA10.md) at `0x0086E270`
- [ObGetObjectInformation](../../page/9D/ObGetObjectInformation_function_009DADE0.md) at `0x009DB133`

### Static image references
- `0x004B136F` → RVA `0x00F0FF80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004B1364  0F B6 41 1A                     movzx eax, byte ptr [rcx + 0x1a]
004B1368  A8 10                           test al, 0x10
004B136A  74 16                           je 0x1404b1382
004B136C  83 E0 1F                        and eax, 0x1f
004B136F  48 8D 15 0A EC A5 00            lea rdx, [rip + 0xa5ec0a]
004B1376  0F B6 04 10                     movzx eax, byte ptr [rax + rdx]
004B137A  48 2B C8                        sub rcx, rax
004B137D  48 8B C1                        mov rax, rcx
004B1380  C3                              ret
004B1381  CC                              int3
004B1382  33 C9                           xor ecx, ecx
004B1384  EB F7                           jmp 0x1404b137d
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall OBJECT_HEADER_TO_PROCESS_INFO(__int64 a1)
{
    __int64 result;

    if ((((unsigned __int8)(*(unsigned __int8 *)(a1 + 26))) & (16)) == 0) goto loc_004B1382;
    result = (unsigned int)((*(unsigned __int8 *)(a1 + 26)) & (31));
    a1 = (a1) - (*(unsigned __int8 *)(result + v_rip + 10873866 * 1));
loc_004B137D:
    return a1;
loc_004B1382:
    a1 = 0;
    goto loc_004B137D;
}
```

## 5. (Beta) C Style

```c
void *OBJECT_HEADER_TO_PROCESS_INFO(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;

    if ((((uint8_t)(*(uint8_t *)(arg1 + 0x1A))) & (16)) == 0) goto loc_004B1382;
    result = (uint32_t)((*(uint8_t *)(arg1 + 0x1A)) & (31));
    Arg1 = (Arg1) - (*(uint8_t *)(result + v_rip + 0xA5EC0A * 1));
loc_004B137D:
    return Arg1;
loc_004B1382:
    Arg1 = 0;
    goto loc_004B137D;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x1A` | `8` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004B1364&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004B1364[BB_004B1364]
  bb_004B136C[BB_004B136C]
  bb_004B137D[BB_004B137D]
  bb_004B1381[BB_004B1381]
  bb_004B1382[BB_004B1382]
  bb_004B1364 -->|branch| bb_004B1382
  bb_004B1364 -->|fallthrough| bb_004B136C
  bb_004B136C -->|flow| bb_004B137D
  bb_004B1381 -->|flow| bb_004B1382
  bb_004B1382 -->|branch| bb_004B137D
```
