# sub_006F77C0

- RVA: `0x006F77C0`–`0x006F77D9` (길이 `25` bytes)
- VA: `0x00000001406F77C0`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000B3D90`
- 디코드: `7`개 명령, `25/25` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x006F77CD` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x006F77D4` → [FsRtlCompleteLockIrpReal + 0x22](../49/FsRtlCompleteLockIrpReal_function_004973AC.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006F77C0  49 8B D0                        mov rdx, r8
006F77C3  41 89 58 30                     mov dword ptr [r8 + 0x30], ebx
006F77C7  49 8B CA                        mov rcx, r10
006F77CA  49 8B C1                        mov rax, r9
006F77CD  E8 FE 32 FC FF                  call 0x1406baad0
006F77D2  8B D8                           mov ebx, eax
006F77D4  E9 F5 FB D9 FF                  jmp 0x1404973ce
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_006F77C0(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;

    *(unsigned int *)(a3 + 48) = (unsigned int)(v_rbx);
    result = guard_dispatch_icall(v_r10, a3, a3, a4);
}
```

## 5. (Beta) C Style

```c
int64_t sub_006F77C0(int64_t Arg1, int64_t Arg2, void *Arg3, int64_t Arg4)
{
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;

    *(uint32_t *)(arg3 + 0x30) = (uint32_t)(local_rbx);
    result = guard_dispatch_icall(local_r10, Arg3, Arg3, Arg4);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg3` | `+ 0x30` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006F77C0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006F77C0[BB_006F77C0]
```
