# MiMakePageAvoidRead$filt$0

- RVA: `0x006D1E5D`–`0x006D1E81` (길이 `36` bytes)
- VA: `0x00000001406D1E5D`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0006DBA0`
- 디코드: `12`개 명령, `36/36` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x006D1E74` → [MiMapCacheExceptionFilter](../../page/A3/MiMapCacheExceptionFilter_function_00A37FA4.md) (function, `0x00A37FA4`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x006D1E74` → [MiMapCacheExceptionFilter](../../page/A3/MiMapCacheExceptionFilter_function_00A37FA4.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
006D1E5D  40 55                           push rbp
006D1E5F  48 83 EC 30                     sub rsp, 0x30
006D1E63  48 8B EA                        mov rbp, rdx
006D1E66  48 89 8D 08 01 00 00            mov qword ptr [rbp + 0x108], rcx
006D1E6D  48 8B D1                        mov rdx, rcx
006D1E70  48 8D 4D 48                     lea rcx, [rbp + 0x48]
006D1E74  E8 2B 61 36 00                  call 0x140a37fa4
006D1E79  90                              nop
006D1E7A  48 83 C4 30                     add rsp, 0x30
006D1E7E  5D                              pop rbp
006D1E7F  C3                              ret
006D1E80  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiMakePageAvoidRead_filt_0(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (48);
    *(unsigned __int64 *)(a2 + 264) = a1;
    result = MiMapCacheExceptionFilter(a2 + 72, a1, a3, a4);
    v_rsp = (v_rsp) + (48);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MiMakePageAvoidRead_filt_0(int64_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (48);
    *(uint64_t *)(arg2 + 0x108) = Arg1;
    result = MiMapCacheExceptionFilter(Arg2 + 72, Arg1, a3, a4);
    local_rsp = (local_rsp) + (48);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x48` | `64` | `R` |
| `Arg2` | `+ 0x108` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006D1E5D&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006D1E5D[BB_006D1E5D]
  bb_006D1E80[BB_006D1E80]
```
