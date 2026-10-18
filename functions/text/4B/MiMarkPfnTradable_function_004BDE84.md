# MiMarkPfnTradable

- RVA: `0x004BDE84`–`0x004BDEAD` (길이 `41` bytes)
- VA: `0x00000001404BDE84`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `14`개 명령, `41/41` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x004BDE8D` → [MiLockPageInline](../31/MiLockPageInline_function_0031A340.md) (function, `0x0031A340`)
- `0x004BDEA1` → [MiUnlockPage](../31/MiUnlockPage_function_0031A3E0.md) (function, `0x0031A3E0`)

### Direct callers
- [MiAllocateProcessShadow](../../page/A5/MiAllocateProcessShadow_function_00A5F1A0.md) at `0x00A5F233`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004BDE84  40 53                           push rbx
004BDE86  48 83 EC 20                     sub rsp, 0x20
004BDE8A  48 8B D9                        mov rbx, rcx
004BDE8D  E8 AE C4 E5 FF                  call 0x14031a340
004BDE92  48 8B 13                        mov rdx, qword ptr [rbx]
004BDE95  48 8B CB                        mov rcx, rbx
004BDE98  48 83 CA 01                     or rdx, 1
004BDE9C  48 89 13                        mov qword ptr [rbx], rdx
004BDE9F  8A D0                           mov dl, al
004BDEA1  E8 3A C5 E5 FF                  call 0x14031a3e0
004BDEA6  48 83 C4 20                     add rsp, 0x20
004BDEAA  5B                              pop rbx
004BDEAB  C3                              ret
004BDEAC  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiMarkPfnTradable(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    result = MiLockPageInline(a1, a2, a3, a4);
    a2 = (*(unsigned __int64 *)(a1)) | (1);
    *(unsigned __int64 *)(a1) = a2;
    result = MiUnlockPage(a1, (unsigned __int8)(result), a3, a4);
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MiMarkPfnTradable(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    result = MiLockPageInline(Arg1, a2, a3, a4);
    a2 = (*(uint64_t *)(arg1)) | (1);
    *(uint64_t *)(arg1) = a2;
    result = MiUnlockPage(Arg1, (uint8_t)(result), a3, a4);
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004BDE84&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004BDE84[BB_004BDE84]
  bb_004BDEAC[BB_004BDEAC]
```
