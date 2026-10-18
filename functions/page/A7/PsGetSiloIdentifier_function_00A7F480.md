# PsGetSiloIdentifier

- RVA: `0x00A7F480`–`0x00A7F48F` (길이 `15` bytes)
- VA: `0x0000000140A7F480`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `6`개 명령, `15/15` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [ObCreateSiloRootDirectory](../83/ObCreateSiloRootDirectory_function_0083CA34.md) at `0x0083CB02`
- [ObGetSiloRootDirectoryPath](../83/ObGetSiloRootDirectoryPath_function_0083CD74.md) at `0x0083CE08`
- [NtQueryInformationProcess](../9A/NtQueryInformationProcess_function_009AA250.md) at `0x009ADE94`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A7F480  33 C0                           xor eax, eax
00A7F482  48 85 C9                        test rcx, rcx
00A7F485  74 06                           je 0x140a7f48d
00A7F487  8B 81 BC 05 00 00               mov eax, dword ptr [rcx + 0x5bc]
00A7F48D  C3                              ret
00A7F48E  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PsGetSiloIdentifier(__int64 a1)
{
    __int64 result;

    result = 0;
    if (a1 != 0) {
        result = *(unsigned int *)(a1 + 1468);
    }
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PsGetSiloIdentifier(int64_t Arg1)
{
    int64_t result;

    result = 0;
    if (Arg1 != 0) {
        result = *(uint32_t *)(Arg1 + 0x5BC);
    }
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A7F480&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A7F480[BB_00A7F480]
  bb_00A7F487[BB_00A7F487]
  bb_00A7F48D[BB_00A7F48D]
  bb_00A7F48E[BB_00A7F48E]
  bb_00A7F480 -->|branch| bb_00A7F48D
  bb_00A7F480 -->|fallthrough| bb_00A7F487
  bb_00A7F487 -->|flow| bb_00A7F48D
```
