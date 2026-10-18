# PfpTraceLogPartitionId

- RVA: `0x005CE1B0`–`0x005CE1C3` (길이 `19` bytes)
- VA: `0x00000001405CE1B0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `7`개 명령, `19/19` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [PfpPartitionCreate](PfpPartitionCreate_function_005CDE8C.md) at `0x005CDEDE`
- [PfpPartitionCreate](PfpPartitionCreate_function_005CDE8C.md) at `0x005CDFB7`
- [PfpTraceLogPfPartitionId](PfpTraceLogPfPartitionId_function_005CE1CC.md) at `0x005CE1DA`
- [PfpPartitionFindOrCreate](../../page/75/PfpPartitionFindOrCreate_function_00752080.md) at `0x007520D2`
- [PfpPartitionFindOrCreate](../../page/75/PfpPartitionFindOrCreate_function_00752080.md) at `0x00752177`
- [sub_00B208F8](../../page/B2/Unknown_function_00B208F8.md) at `0x00B208FB`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005CE1B0  33 C0                           xor eax, eax
005CE1B2  48 85 C9                        test rcx, rcx
005CE1B5  74 0A                           je 0x1405ce1c1
005CE1B7  48 8B 41 78                     mov rax, qword ptr [rcx + 0x78]
005CE1BB  8B 80 D0 01 00 00               mov eax, dword ptr [rax + 0x1d0]
005CE1C1  C3                              ret
005CE1C2  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PfpTraceLogPartitionId(__int64 a1)
{
    __int64 result;

    result = 0;
    if (a1 != 0) {
        result = *(unsigned __int64 *)(a1 + 120);
        result = *(unsigned int *)(result + 464);
    }
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PfpTraceLogPartitionId(int64_t Arg1)
{
    int64_t result;

    result = 0;
    if (Arg1 != 0) {
        result = *(uint64_t *)(Arg1 + 0x78);
        result = *(uint32_t *)(result + 0x1D0);
    }
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005CE1B0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005CE1B0[BB_005CE1B0]
  bb_005CE1B7[BB_005CE1B7]
  bb_005CE1C1[BB_005CE1C1]
  bb_005CE1C2[BB_005CE1C2]
  bb_005CE1B0 -->|branch| bb_005CE1C1
  bb_005CE1B0 -->|fallthrough| bb_005CE1B7
  bb_005CE1B7 -->|flow| bb_005CE1C1
```
