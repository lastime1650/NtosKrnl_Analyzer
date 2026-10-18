# AlpcpDeleteView

- RVA: `0x0088A26C`–`0x0088A298` (길이 `44` bytes)
- VA: `0x000000014088A26C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00065BAC`
- 디코드: `16`개 명령, `44/44` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **6**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0088A275` → [AlpcpDeleteBlob](AlpcpDeleteBlob_function_0088A11C.md) (function, `0x0088A11C`)
- `0x0088A286` → [AlpcpDereferenceBlobEx](AlpcpDereferenceBlobEx_function_0088AF00.md) (function, `0x0088AF00`)

### Direct callers
- [NtAlpcCreateSectionView](NtAlpcCreateSectionView_function_00888640.md) at `0x00888858`
- [AlpcpCaptureViewAttribute](AlpcpCaptureViewAttribute_function_0088957C.md) at `0x00889628`
- [AlpcpCaptureViewAttributeInternal](AlpcpCaptureViewAttributeInternal_function_00889C6C.md) at `0x00889CD3`
- [AlpcpExposeViewAttributeInSenderContext](AlpcpExposeViewAttributeInSenderContext_function_0088F600.md) at `0x0088F70E`
- [NtAlpcDeleteSectionView](../A2/NtAlpcDeleteSectionView_function_00A2F240.md) at `0x00A2F340`
- [AlpcpReleaseViewAttribute](../A6/AlpcpReleaseViewAttribute_function_00A63A80.md) at `0x00A63AC4`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0088A26C  40 53                           push rbx
0088A26E  48 83 EC 20                     sub rsp, 0x20
0088A272  48 8B D9                        mov rbx, rcx
0088A275  E8 A2 FE FF FF                  call 0x14088a11c
0088A27A  84 C0                           test al, al
0088A27C  74 16                           je 0x14088a294
0088A27E  BA 01 00 00 00                  mov edx, 1
0088A283  48 8B CB                        mov rcx, rbx
0088A286  E8 75 0C 00 00                  call 0x14088af00
0088A28B  B0 01                           mov al, 1
0088A28D  48 83 C4 20                     add rsp, 0x20
0088A291  5B                              pop rbx
0088A292  C3                              ret
0088A293  CC                              int3
0088A294  32 C0                           xor al, al
0088A296  EB F5                           jmp 0x14088a28d
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall AlpcpDeleteView(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    result = AlpcpDeleteBlob(a1, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0088A294;
    result = AlpcpDereferenceBlobEx(a1, 1, a3, a4);
loc_0088A28D:
    v_rsp = (v_rsp) + (32);
    return 1;
loc_0088A294:
    result = 0;
    goto loc_0088A28D;
}
```

## 5. (Beta) C Style

```c
int64_t AlpcpDeleteView(int64_t Arg1)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    result = AlpcpDeleteBlob(Arg1, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_0088A294;
    result = AlpcpDereferenceBlobEx(Arg1, 1, a3, a4);
loc_0088A28D:
    local_rsp = (local_rsp) + (32);
    return 1;
loc_0088A294:
    result = 0;
    goto loc_0088A28D;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0088A26C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0088A26C[BB_0088A26C]
  bb_0088A27E[BB_0088A27E]
  bb_0088A28D[BB_0088A28D]
  bb_0088A293[BB_0088A293]
  bb_0088A294[BB_0088A294]
  bb_0088A26C -->|branch| bb_0088A294
  bb_0088A26C -->|fallthrough| bb_0088A27E
  bb_0088A27E -->|flow| bb_0088A28D
  bb_0088A293 -->|flow| bb_0088A294
  bb_0088A294 -->|branch| bb_0088A28D
```
