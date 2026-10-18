# sub_006F0328

- RVA: `0x006F0328`–`0x006F033D` (길이 `21` bytes)
- VA: `0x00000001406F0328`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A6130`
- 디코드: `3`개 명령, `21/21` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x006F032F` → RVA `0x006CD690` (` ?? ::FNODOBFM::`string'`; read)
- `0x006F0336` → RVA `0x006CD6B0` (` ?? ::FNODOBFM::`string'`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
006F0328  44 38 AD 20 02 00 00            cmp byte ptr [rbp + 0x220], r13b
006F032F  48 8D 0D 5A D3 FD FF            lea rcx, [rip - 0x22ca6]
006F0336  48 8D 05 73 D3 FD FF            lea rax, [rip - 0x22c8d]
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_006F0328(void)
{
    return v_rip - 142477;
}
```

## 5. (Beta) C Style

```c
void sub_006F0328(void)
{
    return v_rip - 142477;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006F0328&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006F0328[BB_006F0328]
```
