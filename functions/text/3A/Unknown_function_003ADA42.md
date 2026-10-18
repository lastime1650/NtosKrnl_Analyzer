# sub_003ADA42

- RVA: `0x003ADA42`–`0x003ADA5F` (길이 `29` bytes)
- VA: `0x00000001403ADA42`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008BD2C`
- 디코드: `6`개 명령, `29/29` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x003ADA55` → [ST_STORE<SM_TRAITS>::StReleaseRegion](ST_STORE_SM_TRAITS_StReleaseRegion_function_003AF138.md) (function, `0x003AF138`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x003ADA49` → [sub_003AD7AD + 0xE1](Unknown_function_003AD7AD.md) (`tail-transfer`)
  - `0x003ADA5A` → [sub_003AD7AD + 0xE1](Unknown_function_003AD7AD.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
003ADA42  45 3B 8B 58 06 00 00            cmp r9d, dword ptr [r11 + 0x658]
003ADA49  0F 84 3F FE FF FF               je 0x1403ad88e
003ADA4F  41 8B D1                        mov edx, r9d
003ADA52  48 8B CB                        mov rcx, rbx
003ADA55  E8 DE 16 00 00                  call 0x1403af138
003ADA5A  E9 2F FE FF FF                  jmp 0x1403ad88e
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_003ADA42(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;

    result = ST_STORE_SM_TRAITS___StReleaseRegion(v_rbx, (unsigned int)(a4), a3, a4);
}
```

## 5. (Beta) C Style

```c
int64_t sub_003ADA42(int64_t Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
{
    int64_t result;

    result = ST_STORE_SM_TRAITS___StReleaseRegion(local_rbx, (uint32_t)(Arg4), Arg3, Arg4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003ADA42&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_003ADA42[BB_003ADA42]
  bb_003ADA4F[BB_003ADA4F]
  bb_003ADA42 -->|fallthrough| bb_003ADA4F
```
