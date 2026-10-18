# CmpRecordRegistryLockAcquire

- RVA: `0x004565F4`–`0x00456612` (길이 `30` bytes)
- VA: `0x00000001404565F4`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CEE8`
- 디코드: `10`개 명령, `30/30` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x004565F8` → [CmpGetThreadInfo](CmpGetThreadInfo_function_00456AB8.md) (function, `0x00456AB8`)
- `0x0045660B` → [CmpThreadInfoLogStack](../4C/CmpThreadInfoLogStack_function_004CA590.md) (function, `0x004CA590`)

### Direct callers
- [CmpLockRegistryExclusive](../../page/84/CmpLockRegistryExclusive_function_0084F9B4.md) at `0x0084FA0C`
- [CmpLockRegistry](../../pagecmrc/BC/CmpLockRegistry_function_00BC9B34.md) at `0x00BC9B93`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004565F4  48 83 EC 28                     sub rsp, 0x28
004565F8  E8 BB 04 00 00                  call 0x140456ab8
004565FD  48 85 C0                        test rax, rax
00456600  74 09                           je 0x14045660b
00456602  FF 40 10                        inc dword ptr [rax + 0x10]
00456605  48 83 C4 28                     add rsp, 0x28
00456609  C3                              ret
0045660A  CC                              int3
0045660B  E8 80 3F 07 00                  call 0x1404ca590
00456610  EB F3                           jmp 0x140456605
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpRecordRegistryLockAcquire(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = CmpGetThreadInfo(a1, a2, a3, a4);
    if (result == 0) goto loc_0045660B;
loc_00456605:
    v_rsp = (v_rsp) + (40);
    return result;
loc_0045660B:
    result = CmpThreadInfoLogStack(a1, a2, a3, a4);
    goto loc_00456605;
}
```

## 5. (Beta) C Style

```c
void CmpRecordRegistryLockAcquire(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = CmpGetThreadInfo(a1, a2, a3, a4);
    if (result == 0) goto loc_0045660B;
loc_00456605:
    local_rsp = (local_rsp) + (40);
    return result;
loc_0045660B:
    result = CmpThreadInfoLogStack(a1, a2, a3, a4);
    goto loc_00456605;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004565F4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004565F4[BB_004565F4]
  bb_00456602[BB_00456602]
  bb_00456605[BB_00456605]
  bb_0045660A[BB_0045660A]
  bb_0045660B[BB_0045660B]
  bb_004565F4 -->|branch| bb_0045660B
  bb_004565F4 -->|fallthrough| bb_00456602
  bb_00456602 -->|flow| bb_00456605
  bb_0045660A -->|flow| bb_0045660B
  bb_0045660B -->|branch| bb_00456605
```
