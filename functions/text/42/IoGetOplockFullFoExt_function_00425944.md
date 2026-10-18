# IoGetOplockFullFoExt

- RVA: `0x00425944`–`0x0042595D` (길이 `25` bytes)
- VA: `0x0000000140425944`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `9`개 명령, `25/25` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [FsRtlpOplockCleanup](FsRtlpOplockCleanup_function_00425030.md) at `0x004250A6`
- [FsRtlpOplockDequeueRH](FsRtlpOplockDequeueRH_function_004258FC.md) at `0x00425907`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00425944  33 C0                           xor eax, eax
00425946  48 85 C9                        test rcx, rcx
00425949  74 10                           je 0x14042595b
0042594B  48 8B 91 D0 00 00 00            mov rdx, qword ptr [rcx + 0xd0]
00425952  48 85 D2                        test rdx, rdx
00425955  74 04                           je 0x14042595b
00425957  48 8B 42 38                     mov rax, qword ptr [rdx + 0x38]
0042595B  C3                              ret
0042595C  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IoGetOplockFullFoExt(__int64 a1)
{
    __int64 result;

    result = 0;
    if (a1 == 0) goto loc_0042595B;
    if (*(unsigned __int64 *)(a1 + 208) != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 208) + 56);
    }
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t IoGetOplockFullFoExt(int64_t Arg1)
{
    int64_t result;

    result = 0;
    if (Arg1 == 0) goto loc_0042595B;
    if (*(uint64_t *)(Arg1 + 0xD0) != 0) {
        result = *(uint64_t *)(*(uint64_t *)(Arg1 + 0xD0) + 0x38);
    }
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00425944&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00425944[BB_00425944]
  bb_0042594B[BB_0042594B]
  bb_00425957[BB_00425957]
  bb_0042595B[BB_0042595B]
  bb_0042595C[BB_0042595C]
  bb_00425944 -->|branch| bb_0042595B
  bb_00425944 -->|fallthrough| bb_0042594B
  bb_0042594B -->|branch| bb_0042595B
  bb_0042594B -->|fallthrough| bb_00425957
  bb_00425957 -->|flow| bb_0042595B
```
