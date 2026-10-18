# CmpRecordRegistryLockSharedAcquire

- RVA: `0x0066ABA4`–`0x0066ABC7` (길이 `35` bytes)
- VA: `0x000000014066ABA4`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `12`개 명령, `35/35` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0066ABAD` → [CmpGetThreadInfo](../45/CmpGetThreadInfo_function_00456AB8.md) (function, `0x00456AB8`)

### Direct callers
- [CmpLockRegistry](../../pagecmrc/BC/CmpLockRegistry_function_00BC9B34.md) at `0x00BC9C10`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0066ABA4  40 53                           push rbx
0066ABA6  48 83 EC 20                     sub rsp, 0x20
0066ABAA  48 8B D9                        mov rbx, rcx
0066ABAD  E8 06 BF DE FF                  call 0x140456ab8
0066ABB2  48 83 78 08 00                  cmp qword ptr [rax + 8], 0
0066ABB7  75 04                           jne 0x14066abbd
0066ABB9  48 89 58 08                     mov qword ptr [rax + 8], rbx
0066ABBD  FF 40 10                        inc dword ptr [rax + 0x10]
0066ABC0  48 83 C4 20                     add rsp, 0x20
0066ABC4  5B                              pop rbx
0066ABC5  C3                              ret
0066ABC6  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpRecordRegistryLockSharedAcquire(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    result = CmpGetThreadInfo(a1, a2, a3, a4);
    if ((*(unsigned __int64 *)(result + 8)) == 0) {
        *(unsigned __int64 *)(result + 8) = a1;
    }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t CmpRecordRegistryLockSharedAcquire(int64_t Arg1)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    result = CmpGetThreadInfo(Arg1, a2, a3, a4);
    if ((*(uint64_t *)(result + 0x8)) == 0) {
        *(uint64_t *)(result + 0x8) = Arg1;
    }
    local_rsp = (local_rsp) + (32);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0066ABA4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0066ABA4[BB_0066ABA4]
  bb_0066ABB9[BB_0066ABB9]
  bb_0066ABBD[BB_0066ABBD]
  bb_0066ABC6[BB_0066ABC6]
  bb_0066ABA4 -->|branch| bb_0066ABBD
  bb_0066ABA4 -->|fallthrough| bb_0066ABB9
  bb_0066ABB9 -->|flow| bb_0066ABBD
```
