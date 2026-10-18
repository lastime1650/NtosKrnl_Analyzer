# PspCheckForInvalidAccessByProtection

- RVA: `0x00A10098`–`0x00A100BF` (길이 `39` bytes)
- VA: `0x0000000140A10098`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `15`개 명령, `39/39` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00A100AA` → [RtlTestProtectedAccess](RtlTestProtectedAccess_function_00A100C8.md) (function, `0x00A100C8`)

### Direct callers
- [PspThreadOpen](../A0/PspThreadOpen_function_00A0FED0.md) at `0x00A0FF63`
- [NtCreateUserProcess](../AE/NtCreateUserProcess_function_00AEA680.md) at `0x00AEB0A5`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A10098  48 83 EC 28                     sub rsp, 0x28
00A1009C  45 32 C9                        xor r9b, r9b
00A1009F  8A C2                           mov al, dl
00A100A1  84 C9                           test cl, cl
00A100A3  74 11                           je 0x140a100b6
00A100A5  41 8A D0                        mov dl, r8b
00A100A8  8A C8                           mov cl, al
00A100AA  E8 19 00 00 00                  call 0x140a100c8
00A100AF  84 C0                           test al, al
00A100B1  75 03                           jne 0x140a100b6
00A100B3  41 B1 01                        mov r9b, 1
00A100B6  41 8A C1                        mov al, r9b
00A100B9  48 83 C4 28                     add rsp, 0x28
00A100BD  C3                              ret
00A100BE  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PspCheckForInvalidAccessByProtection(unsigned __int8 a1, unsigned __int8 a2, unsigned __int8 a3, unsigned __int8 a4)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    a4 = 0;
    if (a1 == 0) goto loc_00A100B6;
    result = RtlTestProtectedAccess(a2, a3, a3, a4);
    if ((unsigned __int8)(result) == 0) {
        a4 = 1;
    }
    v_rsp = (v_rsp) + (40);
    return a4;
}
```

## 5. (Beta) C Style

```c
int64_t PspCheckForInvalidAccessByProtection(uint8_t Arg1, uint8_t Arg2, uint8_t Arg3, uint8_t Arg4)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    Arg4 = 0;
    if (Arg1 == 0) goto loc_00A100B6;
    result = RtlTestProtectedAccess(Arg2, Arg3, Arg3, Arg4);
    if ((uint8_t)(result) == 0) {
        Arg4 = 1;
    }
    local_rsp = (local_rsp) + (40);
    return Arg4;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A10098&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A10098[BB_00A10098]
  bb_00A100A5[BB_00A100A5]
  bb_00A100B3[BB_00A100B3]
  bb_00A100B6[BB_00A100B6]
  bb_00A100BE[BB_00A100BE]
  bb_00A10098 -->|branch| bb_00A100B6
  bb_00A10098 -->|fallthrough| bb_00A100A5
  bb_00A100A5 -->|branch| bb_00A100B6
  bb_00A100A5 -->|fallthrough| bb_00A100B3
  bb_00A100B3 -->|flow| bb_00A100B6
```
