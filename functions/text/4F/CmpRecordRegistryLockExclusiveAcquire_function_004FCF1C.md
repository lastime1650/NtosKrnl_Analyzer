# CmpRecordRegistryLockExclusiveAcquire

- RVA: `0x004FCF1C`–`0x004FCF3D` (길이 `33` bytes)
- VA: `0x00000001404FCF1C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `9`개 명령, `33/33` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x004FCF20` → [CmpGetThreadInfo](../45/CmpGetThreadInfo_function_00456AB8.md) (function, `0x00456AB8`)

### Direct callers
- [CmpLockRegistryExclusive](../../page/84/CmpLockRegistryExclusive_function_0084F9B4.md) at `0x0084F9FB`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004FCF1C  48 83 EC 28                     sub rsp, 0x28
004FCF20  E8 93 9B F5 FF                  call 0x140456ab8
004FCF25  48 83 78 08 00                  cmp qword ptr [rax + 8], 0
004FCF2A  75 08                           jne 0x1404fcf34
004FCF2C  48 C7 40 08 01 00 00 00         mov qword ptr [rax + 8], 1
004FCF34  FF 40 10                        inc dword ptr [rax + 0x10]
004FCF37  48 83 C4 28                     add rsp, 0x28
004FCF3B  C3                              ret
004FCF3C  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpRecordRegistryLockExclusiveAcquire(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = CmpGetThreadInfo(a1, a2, a3, a4);
    if ((*(unsigned __int64 *)(result + 8)) == 0) {
        *(unsigned __int64 *)(result + 8) = 1;
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void CmpRecordRegistryLockExclusiveAcquire(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = CmpGetThreadInfo(a1, a2, a3, a4);
    if ((*(uint64_t *)(result + 0x8)) == 0) {
        *(uint64_t *)(result + 0x8) = 1;
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004FCF1C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004FCF1C[BB_004FCF1C]
  bb_004FCF2C[BB_004FCF2C]
  bb_004FCF34[BB_004FCF34]
  bb_004FCF3C[BB_004FCF3C]
  bb_004FCF1C -->|branch| bb_004FCF34
  bb_004FCF1C -->|fallthrough| bb_004FCF2C
  bb_004FCF2C -->|flow| bb_004FCF34
```
