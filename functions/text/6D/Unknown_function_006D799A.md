# sub_006D799A

- RVA: `0x006D799A`–`0x006D79A9` (길이 `15` bytes)
- VA: `0x00000001406D799A`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00060E4C`
- 디코드: `4`개 명령, `15/15` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x006D799D` → [MiUnlockAndDereferenceVad](../31/MiUnlockAndDereferenceVad_function_00316E60.md) (function, `0x00316E60`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x006D79A4` → [MiProbeAndLockPrepare + 0x14E](../23/MiProbeAndLockPrepare_function_0023BB40.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006D799A  48 8B CF                        mov rcx, rdi
006D799D  E8 BE F4 C3 FF                  call 0x140316e60
006D79A2  8B C3                           mov eax, ebx
006D79A4  E9 E5 42 B6 FF                  jmp 0x14023bc8e
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_006D799A(void)
{
    __int64 result;

    result = MiUnlockAndDereferenceVad(v_rdi, a2, a3, a4);
}
```

## 5. (Beta) C Style

```c
void sub_006D799A(void)
{
    int64_t result;

    result = MiUnlockAndDereferenceVad(local_rdi, a2, a3, a4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006D799A&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006D799A[BB_006D799A]
```
