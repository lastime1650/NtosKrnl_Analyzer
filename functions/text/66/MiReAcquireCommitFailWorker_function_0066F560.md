# MiReAcquireCommitFailWorker

- RVA: `0x0066F560`–`0x0066F58F` (길이 `47` bytes)
- VA: `0x000000014066F560`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `14`개 명령, `47/47` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0066F56E` → [PsTerminateProcess](../../page/90/PsTerminateProcess_function_00904C64.md) (function, `0x00904C64`)
- `0x0066F576` → [KeForceResumeProcess](../3C/KeForceResumeProcess_function_003C1BE4.md) (function, `0x003C1BE4`)
- `0x0066F583` → [ObfDereferenceObjectWithTag](../2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0066F56E` → [PsTerminateProcess](../../page/90/PsTerminateProcess_function_00904C64.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0066F560  40 53                           push rbx
0066F562  48 83 EC 20                     sub rsp, 0x20
0066F566  BA 2D 01 00 C0                  mov edx, 0xc000012d
0066F56B  48 8B D9                        mov rbx, rcx
0066F56E  E8 F1 56 29 00                  call 0x140904c64
0066F573  48 8B CB                        mov rcx, rbx
0066F576  E8 69 26 D5 FF                  call 0x1403c1be4
0066F57B  BA 4D 6D 50 72                  mov edx, 0x72506d4d
0066F580  48 8B CB                        mov rcx, rbx
0066F583  E8 58 83 C8 FF                  call 0x1402f78e0
0066F588  48 83 C4 20                     add rsp, 0x20
0066F58C  5B                              pop rbx
0066F58D  C3                              ret
0066F58E  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiReAcquireCommitFailWorker(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    result = PsTerminateProcess(a1, (unsigned int)(0xC000012DULL), a3, a4);
    result = KeForceResumeProcess(a1, (unsigned int)(0xC000012DULL), a3, a4);
    result = ObfDereferenceObjectWithTag(a1, (unsigned int)(0x72506D4DULL), a3, a4);
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MiReAcquireCommitFailWorker(int64_t Arg1)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    result = PsTerminateProcess(Arg1, (uint32_t)(0xC000012DULL), a3, a4);
    result = KeForceResumeProcess(Arg1, (uint32_t)(0xC000012DULL), a3, a4);
    result = ObfDereferenceObjectWithTag(Arg1, (uint32_t)(0x72506D4DULL), a3, a4);
    local_rsp = (local_rsp) + (32);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0066F560&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0066F560[BB_0066F560]
  bb_0066F58E[BB_0066F58E]
```
