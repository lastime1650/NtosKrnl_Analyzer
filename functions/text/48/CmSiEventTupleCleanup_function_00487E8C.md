# CmSiEventTupleCleanup

- RVA: `0x00487E8C`–`0x00487EBC` (길이 `48` bytes)
- VA: `0x0000000140487E8C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `16`개 명령, `48/48` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00487EA3` → [ObfDereferenceObjectWithTag](../2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00487EB0` → [ZwClose](../6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)

### Direct callers
- [CmpHiveCacheEntryCleanup](../../page/7F/CmpHiveCacheEntryCleanup_function_007F5B38.md) at `0x007F5C6E`
- [CmpOpenHiveFile](../../page/87/CmpOpenHiveFile_function_0087A71C.md) at `0x0087AB08`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00487E8C  40 53                           push rbx
00487E8E  48 83 EC 20                     sub rsp, 0x20
00487E92  48 8B D9                        mov rbx, rcx
00487E95  48 8B 49 08                     mov rcx, qword ptr [rcx + 8]
00487E99  48 85 C9                        test rcx, rcx
00487E9C  74 0A                           je 0x140487ea8
00487E9E  BA 44 66 6C 74                  mov edx, 0x746c6644
00487EA3  E8 38 FA E6 FF                  call 0x1402f78e0
00487EA8  48 8B 0B                        mov rcx, qword ptr [rbx]
00487EAB  48 85 C9                        test rcx, rcx
00487EAE  74 05                           je 0x140487eb5
00487EB0  E8 FB 53 22 00                  call 0x1406ad2b0
00487EB5  48 83 C4 20                     add rsp, 0x20
00487EB9  5B                              pop rbx
00487EBA  C3                              ret
00487EBB  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmSiEventTupleCleanup(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    if (*(unsigned __int64 *)(a1 + 8) != 0) {
        a2 = 0x746C6644ULL;
        result = ObfDereferenceObjectWithTag(*(unsigned __int64 *)(a1 + 8), a2, a3, a4);
    }
    if (*(unsigned __int64 *)(a1) != 0) {
        result = ZwClose(*(unsigned __int64 *)(a1), a2, a3, a4);
    }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t CmSiEventTupleCleanup(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    if (*(uint64_t *)(arg1 + 0x8) != 0) {
        a2 = 0x746C6644ULL;
        result = ObfDereferenceObjectWithTag(*(uint64_t *)(arg1 + 0x8), a2, a3, a4);
    }
    if (*(uint64_t *)(arg1) != 0) {
        result = ZwClose(*(uint64_t *)(arg1), a2, a3, a4);
    }
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00487E8C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00487E8C[BB_00487E8C]
  bb_00487E9E[BB_00487E9E]
  bb_00487EA8[BB_00487EA8]
  bb_00487EB0[BB_00487EB0]
  bb_00487EB5[BB_00487EB5]
  bb_00487EBB[BB_00487EBB]
  bb_00487E8C -->|branch| bb_00487EA8
  bb_00487E8C -->|fallthrough| bb_00487E9E
  bb_00487E9E -->|flow| bb_00487EA8
  bb_00487EA8 -->|branch| bb_00487EB5
  bb_00487EA8 -->|fallthrough| bb_00487EB0
  bb_00487EB0 -->|flow| bb_00487EB5
```
