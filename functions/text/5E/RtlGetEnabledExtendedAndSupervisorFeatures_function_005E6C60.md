# RtlGetEnabledExtendedAndSupervisorFeatures

- RVA: `0x005E6C60`–`0x005E6C7F` (길이 `31` bytes)
- VA: `0x00000001405E6C60`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `7`개 명령, `31/31` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005E6C60  48 B8 F0 05 00 00 80 F7 FF FF   movabs rax, 0xfffff780000005f0
005E6C6A  48 BA D8 03 00 00 80 F7 FF FF   movabs rdx, 0xfffff780000003d8
005E6C74  48 8B 00                        mov rax, qword ptr [rax]
005E6C77  48 0B 02                        or rax, qword ptr [rdx]
005E6C7A  48 23 C1                        and rax, rcx
005E6C7D  C3                              ret
005E6C7E  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlGetEnabledExtendedAndSupervisorFeatures(__int64 a1)
{
    __int64 result;

    result = (*(unsigned __int64 *)(result)) | (*(unsigned __int64 *)(a2));
    result = (result) & (a1);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t RtlGetEnabledExtendedAndSupervisorFeatures(int64_t Arg1)
{
    int64_t result;

    result = (*(uint64_t *)(result)) | (*(uint64_t *)(a2));
    result = (result) & (Arg1);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005E6C60&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005E6C60[BB_005E6C60]
  bb_005E6C7E[BB_005E6C7E]
```
